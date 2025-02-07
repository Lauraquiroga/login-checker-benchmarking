from .utils import Helper

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

    @Helper.timing_decorator 
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
        result = login in self.hashData
        return result