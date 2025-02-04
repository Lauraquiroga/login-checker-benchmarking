import time
import math
import mmh3
from bitarray import bitarray


class BloomFilter:
    '''
    Class implementing a Bloom filter, using murmur3 hash function.

    A Bloom filter is a space-efficient probabilistic data structure used to check for existence over a set.
    Frequently described as a 'space-optimized' version of hashing,
    It supports element insertion and, with a very low False Positive probability, existence check.
    It does not support deletion.

    Bloom filters were originally described in:
        Bloom, B. H. (1970). 
        Space/time trade-offs in hash coding with allowable errors. 
        Communications of the ACM, 13(7), 422-426.
    
    Code adapted from: https://www.geeksforgeeks.org/bloom-filters-introduction-and-python-implementation/
    '''

    def __init__(self, data_size, fp_prob):
        '''
        Initialize Bloom Filter parameters
        
        Parameters:
        data_size (int): Number of elements expected to be stored in bloom filter (should always be greater than 0)
        fp_prob (float): False Positive probability in decimal
        '''
        # False possible probability in decimal
        self.fp_prob = fp_prob

        # Size of bit array to use
        self.size = self.calculate_size(data_size, fp_prob)

        # Number of hash functions to use (k)
        self.k = self.get_hash_count(self.size, data_size)

        # Bit array of given size
        self.bit_array = bitarray(self.size)

        # Initialize all bits as 0
        self.bit_array.setall(0)

    def exists(self, login):
        """
        Checks if a given username exists in the Bloom Filter.

        Parameters:
        login (str): The username to search for.

        Returns:
        bool: True if there is probability that the username exists in the dataset, False otherwise.
        float: Time elapsed to find result
        """
        start_time = time.perf_counter()
        for i in range(self.k):
            digest = mmh3.hash(login, i) % self.size
            if self.bit_array[digest] == False:
                # if any of bit is False then,its not present in filter (certain, no False Negatives)
                # else there is 1-self.fp_prob probability that it exist
                elapsed_time = time.perf_counter() - start_time
                return False, elapsed_time
        elapsed_time = time.perf_counter() - start_time
        return True, elapsed_time

    def initialize_with_dataset(self, dataset):
        """
        Initialize the Bloom filter with a dataset.

        Parameters:
        dataset (iterable): The dataset to initialize the filter with.
        """
        for login in dataset:
            for i in range(self.k):
                # i work as seed to mmh3.hash() function
                # With different seed, digest created is different
                digest = mmh3.hash(login, i) % self.size
                self.bit_array[digest] = True

    @classmethod
    def calculate_size(self, n, fp):
        '''
        Calcuates the size of bit array(m) to use using the following formula:
        m = -(n * lg(p)) / (lg(2)^2)

        Parameters:
        n (int): Number of items expected to be stored in filter
        p (float): False Positive probability in decimal

        Return: 
        int: The size of the bit array (m)
        '''
        m = -(n * math.log(fp))/(math.log(2)**2)
        return int(m)

    @classmethod
    def get_hash_count(self, m, n):
        '''
        Calculates the number of hash functions (k) to be used to calculate the hashes for a given input
        following formula: k = (m/n) * lg(2)

        Parameters:
        m (int): size of bit array
        n (int): number of items expected to be stored in filter

        Return:
        int: Number of hash functions (k)
        '''
        k = (m/n) * math.log(2)
        return int(k)