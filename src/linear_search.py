import time

class LinearSearch:
    @staticmethod
    def exists(data, login):
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
        for element in data:
            if login==element:
                elapsed_time = time.perf_counter() - start_time
                return True, elapsed_time
        elapsed_time = time.perf_counter() - start_time
        return False, elapsed_time