from .base_algorithm import BaseAlgorithm
from .utils import Helper

class LinearSearch(BaseAlgorithm):
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

    @Helper.timing_decorator 
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
        for element in self.data:
            if login==element:
                return True
        return False