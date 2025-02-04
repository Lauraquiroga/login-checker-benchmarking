import time

class BinarySearch:
    def __init__(self, data, login):
        self.login = login
        self.orderedData = sorted(data)

    def exists(self):
        """
        Implementation of a binary search algorithm over an ordered list.

        Parameters:
        orderedData (list of str): The dataset to search within (ordered).
        login (str): The username to search for.

        Returns:
        bool: True if the username exists in the dataset, False otherwise.
        float: Time elapsed to find result
        """
        start_time = time.perf_counter()        
        low = 0
        high = len(self.orderedData)-1
        while low<=high:
            mid = (high+low)//2
            if self.orderedData[mid]==self.login:
                elapsed_time = time.time() - start_time
                return True, elapsed_time
            elif self.orderedData[mid]<self.login:
                low = mid+1
            elif self.orderedData[mid]>self.login:
                high = mid-1
        elapsed_time = time.perf_counter() - start_time
        return False, elapsed_time