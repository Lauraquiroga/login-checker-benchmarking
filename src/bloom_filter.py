import time

class BloomFilter:
    def __init__(self, data, login):
        self.login = login

    def exists(self):
        """
        Checks if a given username exists in the hash table.

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