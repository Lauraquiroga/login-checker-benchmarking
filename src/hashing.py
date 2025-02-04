import time

class Hashing:
    def __init__(self, data, login):
        # Storing data as a hash table (dict)
        self.hashData = set(data)
        self.login = login

    def exists(self):
        """
        Checks if a given username exists in the hash table.

        Parameters:
        hash_set (set): The dataset to search within.
        login (str): The username to search for.

        Returns:
        bool: True if the username exists in the dataset, False otherwise.
        float: Time elapsed to fin result
        """
        start_time = time.time()
        result = self.login in self.hash_set
        elapsed_time = time.time() - start_time
        return result, elapsed_time