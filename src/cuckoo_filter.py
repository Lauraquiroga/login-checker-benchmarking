import time
import mmh3
import math

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
    def __init__(self, capacity, f, b=2, max_evictions=500):
        """
        Initialize Cuckoo Filter parameters

        Parameters:
        capacity (int): Defines the number of buckets the filter contains
        f (int): The size of the fingerprints in bytes
        b (int): The bucket size (number of entries a bucket can hold)
        max_evictions (int): Maximum number of evictions of an entry before deciding the filter is full
        """
        self.capacity = capacity
        self.fingerprint_size = f
        self.bucket_size = b
        self.max_evictions = max_evictions

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
        ## Implement algorithm
        elapsed_time = time.perf_counter() - start_time
        return False, elapsed_time