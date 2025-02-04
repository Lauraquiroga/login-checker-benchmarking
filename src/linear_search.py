import time

class LinearSearch:
    """
    Class implementing a Linear Search algorithm
    """
    def __init__(self, data):
        """
        Initialize data from given list

        Parameters:
        data (list of str): dataset to search within
        """
        self.data = data

    def exists(self, login):
        """
        Implementation of a linear search algorithm over an unordered list.

        Parameters:
        data (list of str): The dataset to search within (unordered).
        login (str): The username to search for.

        Returns:
        bool: True if the username exists in the dataset, False otherwise.
        float: Time elapsed to find result
        """
        start_time = time.perf_counter()
        for element in self.data:
            if login==element:
                elapsed_time = time.perf_counter() - start_time
                return True, elapsed_time
        elapsed_time = time.perf_counter() - start_time
        return False, elapsed_time