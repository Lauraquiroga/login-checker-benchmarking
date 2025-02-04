import time

class Hashing:
    """
    Class implementing hashing
    """
    def __init__(self, data):
        """
        Initialize Hashing structure:
        Store data as a hash table (set)

        Parameters:
        data (list of str): dataset to search within
        """
        self.hashData = set(data)

    def exists(self, login) :
        """
        Checks if a given username exists in the hash table.

        Parameters:
        hash_set (set): The dataset to search within.
        login (str): The username to search for.

        Returns:
        bool: True if the username exists in the dataset, False otherwise.
        float: Time elapsed to find result
        """
        start_time = time.perf_counter()
        result = login in self.hashData
        elapsed_time = time.perf_counter() - start_time
        return result, elapsed_time