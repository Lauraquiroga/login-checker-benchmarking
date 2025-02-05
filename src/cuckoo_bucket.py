import random


class Bucket:
    '''
    Implementation of the Bucket class for storing fingerprints in the Cuckoo Filter.
    
    Code adapted from: https://github.com/michael-the1/python-cuckoo
    '''

    def __init__(self, size):
        '''
        Initialize bucket.
        
        Parameters:
        size (int): the maximum number of fingerprints a bucket can store
        '''
        self.size = size
        self.b = []

    def insert(self, fingerprint):
        '''
        Insert a fingerprint into the bucket.
        The insertion of duplicate entries is allowed.

        Parameters:
        fingerprint ():
        '''
        if not self.is_full():
            self.b.append(fingerprint)
            return True
        return False

    def contains(self, fingerprint):
        return fingerprint in self.b

    def delete(self, fingerprint):
        '''
        Delete a fingerprint from the bucket.

        Returns True if the fingerprint was present in the bucket.
        This is useful for keeping track of how many items are present in the filter.
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
        
        The given fingerprint is stored in the bucket.
        The swapped fingerprint is returned.
        '''
        bucket_index = random.choice(range(len(self.b)))
        fingerprint, self.b[bucket_index] = self.b[bucket_index], fingerprint
        return fingerprint

    def is_full(self):
        return len(self.b) >= self.size

    def __contains__(self, fingerprint):
        return self.contains(fingerprint)

    def __repr__(self):
        return '<Bucket: ' + str(self.b) + '>'

    def __sizeof__(self):
        return super().__sizeof__() + self.b.__sizeof__()