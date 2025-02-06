import time
import mmh3
import math
import random
from .cuckoo_bucket import Bucket

class CuckooFilter:
    """
    Class implementing a Cuckoo filter, using murmur3 hash function.

    A Cuckoo filter is a space-efficient probabilistic data structure used to check for existence over a set.
    It supports element insertion and, with a very low False Positive probability, existence check.
    More efficient than a Bloom Filter and supports element deletion.

    Cuckoo filters were originally described in:
        Fan, B., Andersen, D. G., Kaminsky, M., & Mitzenmacher, M. D. (2014, December).
        Cuckoo filter: Practically better than bloom.
        In Proceedings of the 10th ACM International on Conference on emerging Networking Experiments and Technologies (pp. 75-88). ACM.

    Code adapted from: https://github.com/michael-the1/python-cuckoo
    """


    def __init__(self, data_size,  fp_prob, b=2, max_evictions=500, load_factor=0.9):
        """
        Initialize Cuckoo Filter parameters

        Parameters:
        data_size (int): Number of elements to be stored in the filter
        fp_prob (float): Target False Positive probability in decimal
        b (int): The bucket size (number of entries a bucket can hold)
        max_evictions (int): Maximum number of evictions of an entry before deciding the filter is full
        load_factor (float): 
        """
        self.bucket_size = b
        self.max_evictions = max_evictions
        self.fp_prob = fp_prob
        self.n = data_size
        self.load_factor = load_factor

        self.capacity = self.calculate_capacity()
        self.fingerprint_size = self.calculate_f_size()

        # Elements currently stored by the filter
        self.stored = 0
        # List of Buckets
        self.buckets = [Bucket(size=b) for _ in range(self.capacity)]

    def calculate_capacity(self):
        """
        Calculates the capacity of the Cuckoo Filter (number of buckets the filter contains).
        
        Defined by the formula:
            m = N / (a x b)

        Where:
            m = the capacity
            N = the number of elements in the dataset to be stored
            a = the load factor
            b = the bucket size (number of slots per bucket)

        Return:
        int: The number of buckets the filter contains
        """
        m = math.ceil(self.n / (self.load_factor * self.bucket_size))
        return m
    
    def calculate_f_size(self):
        """
        Calculates the fingerprint size in bytes.

        Defined bythe formula:
            f >= log_2(2b/fp_prob)

        Where:
            f = Fingerprint size
            b = The bucket size (number of slots per bucket)
            fpp = False Positive probability in decimal

        We will use the size as: log_2(2b/fpp)
        
        Return:
        int: The size of the fingerprints in bytes
        """
        f_bits = math.ceil(math.log2(2 * self.bucket_size / self.fp_prob))
        f_bytes = math.ceil(f_bits / 8)  # Convert to bytes
        return f_bytes

    def fingerprint(self, item):
        '''
        Calculates the fingerprint by hashing the item (with MurmurHash3) and truncating the hash to the given length
        The length of the fingerprint is given by fingerprint_size.
        
        Parameters:
        item (str): The string for which the fingerprint must be calculated

        Return:
        bytes: The calculated fingerprint of length fingerprint_size
        '''
        item_hash = mmh3.hash_bytes(item)
        return item_hash[:self.fingerprint_size]
    
    def index_hash(self, item):
        '''
        Calculate the (first) index of an item in the filter.

        Parameters:
        item (str):

        Return:

        '''
        item_hash = mmh3.hash_bytes(item)
        index = int.from_bytes(item_hash, byteorder='big') % self.capacity # Modulo: to keep the index within bounds
        return index
    
    def potential_buckets(self, item, fingerprint):
        '''
        Compute the alternative index for storing an item

        Parameters:
        item (str): The string to be inserted in the filter

        Return
        int: Primary index to store item
        int: Secondary (alternative) index to store item
        '''
        # Primary index: h1(item) = hash(item)
        i1 = self.index_hash(item)

        # Alternative index: h2(item) = h1(item) XOR hash(fingerprint)
        i2 = (i1 ^ self.index_hash(fingerprint)) % self.capacity # Modulo: to keep the index within bounds
        return i1, i2
    
    def insert(self, login):
        """
        Inserts an element in the filter

        Parameters:
        login (str): The login item to be inserted

        Return:
        int: index where the item (login) was inserted

        Throws an exception if the insertion fails -> If filter is determined to be full
        """
        self.stored += 1
        fingerprint = self.fingerprint(login)
        i1, i2 = self.potential_buckets(login, fingerprint)

        # Try insertion
        if self.buckets[i1].insert(fingerprint):
            return i1
        elif self.buckets[i2].insert(fingerprint):
            return i2
        
        # Eviction: If both buckets are full
        i = random.choice((i1, i2)) # Randomly select one of the buckets for eviction

        # Continue until new element and evicted one(s) are placed into buckets or until max. number of evictions is reached
        for evictions in range(self.max_evictions):
            # Evict the fingerprint at i
            fingerprint = self.buckets[i].swap(fingerprint)
            # Recompute alternative index for evicted fingerprint
            i = (i ^ self.index_hash(fingerprint)) % self.capacity
            # Try insertion of evicted fingerprint
            if self.buckets[i].insert(fingerprint):
                return i

        self.stored = self.stored - 1
        raise Exception('Filter is full')
    
    def initialize_with_dataset(self, logins):
        """
        Inserts multiple login elements into the filter.

        Parameters:
        logins (list of str): A list of login items to be inserted.

        Returns:
        int: Number of successfully inserted logins.
        
        Raises:
        Exception: If the filter becomes full before all insertions are completed.
        """
        successful_insertions = 0

        for login in logins:
            try:
                self.insert(login)
                successful_insertions += 1
            except Exception as e:
                print(f"Failed to insert {login}: {e}")
                break  # Stop inserting if the filter is full
        
        return successful_insertions


    def exists(self, login):
        """
        Checks if a given username exists in the Cuckoo filter.

        Parameters:
        login (str): The username to search for.

        Returns:
        bool: True if the username exists in the dataset, False otherwise.
        float: Time elapsed to find result
        """
        start_time = time.perf_counter()

        fingerprint = self.fingerprint(login)
        i1, i2 = self.potential_buckets(login, fingerprint)
        result = (fingerprint in self.buckets[i1]) or (fingerprint in self.buckets[i2])

        elapsed_time = time.perf_counter() - start_time
        return result, elapsed_time