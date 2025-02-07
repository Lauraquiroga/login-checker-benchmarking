from .base_algorithm import BaseAlgorithm
from .utils import Helper

class BinarySearch(BaseAlgorithm):
    """
    Class implementing a Binary Search algorithm
    """
    def __init__(self, data):
        """
        Initialize structure for binary search:
        Store ordered data

        Parameters:
        data (list of str): dataset to search within
        """
        self.orderedData = sorted(data)

    @Helper.timing_decorator 
    def exists(self, login):
        """
        Implementation of a binary search algorithm over an ordered list.

        Parameters:
        orderedData (list of str): The dataset to search within (ordered).
        login (str): The username to search for.

        Returns:
        bool: True if the username exists in the dataset, False otherwise.
        float: Time elapsed to find result
        """      
        low = 0
        high = len(self.orderedData)-1
        while low<=high:
            mid = (high+low)//2
            if self.orderedData[mid]==login:
                return True
            elif self.orderedData[mid]<login:
                low = mid+1
            elif self.orderedData[mid]>login:
                high = mid-1
        return False