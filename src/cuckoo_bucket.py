import random


class Bucket:
    '''
    Implementation of the Bucket class for storing fingerprints in the Cuckoo Filter.
    
    This class provides methods to insert, delete, check for presence, and swap fingerprints 
    within a bucket. It also tracks whether the bucket is full, and supports custom 
    serialization through the `__repr__` and `__sizeof__` methods.

    Code adapted from: https://github.com/michael-the1/python-cuckoo
    '''

    def __init__(self, size):
        '''
        Initialize the bucket with a maximum size.

        The bucket can store fingerprints, with a maximum limit defined by the `size` parameter.

        Parameters:
        size (int): the maximum number of fingerprints a bucket can store
        '''
        self.size = size
        self.b = []

    def insert(self, fingerprint):
        '''
        Insert a fingerprint into the bucket.

        Insertion of duplicate entries is allowed, meaning multiple occurrences of 
        the same fingerprint can be stored in the bucket.

        Parameters:
        fingerprint: The fingerprint to be inserted into the bucket.

        Returns:
        bool: True if the fingerprint was inserted successfully, False if the bucket is full.
        '''
        if not self.is_full():
            self.b.append(fingerprint)
            return True
        return False

    def contains(self, fingerprint):
        '''
        Check if a fingerprint is present in the bucket.

        Parameters:
        fingerprint: The fingerprint to check for in the bucket.

        Returns:
        bool: True if the fingerprint is present, False otherwise.
        '''
        return fingerprint in self.b

    def delete(self, fingerprint):
        '''
        Delete a fingerprint from the bucket.

        This method attempts to delete the given fingerprint from the bucket. 
        If the fingerprint is present, it is removed. If it's not, no error is raised.

        Parameters:
        fingerprint: The fingerprint to be deleted.

        Returns:
        bool: True if the fingerprint was present and deleted, False if the fingerprint was not found.
        '''
        try:
            del self.b[self.b.index(fingerprint)]
            return True
        except ValueError:
            # This error is explicitly silenced.
            # It simply means the fingerprint was never present in the bucket.
            return False

    def swap(self, fingerprint):
        '''
        Swap a fingerprint with a randomly chosen fingerprint from the bucket.

        The given fingerprint is stored in the bucket, and a random fingerprint from the
        bucket is returned in exchange.

        Parameters:
        fingerprint: The fingerprint to be inserted into the bucket.

        Returns:
        fingerprint: The randomly chosen fingerprint that was swapped out.
        '''
        bucket_index = random.choice(range(len(self.b)))
        fingerprint, self.b[bucket_index] = self.b[bucket_index], fingerprint
        return fingerprint

    def is_full(self):
        '''
        Check if the bucket is full.

        Returns:
        bool: True if the bucket has reached its maximum size, False otherwise.
        '''
        return len(self.b) >= self.size

    def __contains__(self, fingerprint):
        '''
        Check if a fingerprint is in the bucket using the `in` operator.

        Parameters:
        fingerprint: The fingerprint to check for in the bucket.

        Returns:
        bool: True if the fingerprint is in the bucket, False otherwise.
        '''
        return self.contains(fingerprint)

    def __repr__(self):
        '''
        String representation of the bucket.

        Returns:
        str: A string representation of the fingerprints stored in the bucket.
        '''
        return '<Bucket: ' + str(self.b) + '>'

    def __sizeof__(self):
        '''
        Get the size of the bucket object in memory.

        Returns:
        int: The size of the bucket object including the memory used by the list of fingerprints.
        '''
        return super().__sizeof__() + self.b.__sizeof__()