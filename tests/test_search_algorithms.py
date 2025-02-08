import unittest
from src.linear_search import LinearSearch
from src.binary_search import BinarySearch

class TestSearchAlgorithms(unittest.TestCase):
    """
    Unit test class for the `LinearSearch` and `BinarySearch` classes, using Python's built-in unittest framework.
    """

    def test_linear_exists_username_found(self):
        """
        Test case for the `LinearSearch` class when the username exists in the dataset.

        This test verifies that the `exists` method of the `LinearSearch` class correctly identifies
        if a given username exists in the list of usernames. The test checks for:
        - Returning `True` when the username is found.
        - Ensuring that the execution time is measured correctly.
        
        Steps:
        1. A list of sample usernames is created.
        2. The `exists` method is called with a username that is in the list.
        3. The test asserts that the result is `True`, indicating the username was found.
        4. The test asserts that the execution time is greater than 0.

        Asserts:
        - True if the username is found.
        - The elapsed time of the method execution is greater than 0.
        """
        usernames = ['user1', 'user2', 'user3']
        username = 'user2'
        linearSearch = LinearSearch(usernames)
        result, elapsed_time = linearSearch.exists(username)
        self.assertTrue(result)  # It should return True for an existing username
        self.assertGreater(elapsed_time, 0)  # Ensure some time was taken

    def test_linear_exists_username_not_found(self):
        """
        Test case for the `LinearSearch` class when the username does not exist in the dataset.

        This test verifies that the `exists` method of the `LinearSearch` class correctly identifies
        if a given username is not in the list of usernames. The test checks for:
        - Returning `False` when the username is not found.
        - Ensuring that the execution time is measured correctly.

        Steps:
        1. A list of sample usernames is created.
        2. The `exists` method is called with a username that is not in the list.
        3. The test asserts that the result is `False`, indicating the username was not found.
        4. The test asserts that the execution time is greater than 0.

        Asserts:
        - False if the username is not found.
        - The elapsed time of the method execution is greater than 0.
        """
        usernames = ['user1', 'user2', 'user3']
        username = 'user4'
        linearSearch = LinearSearch(usernames)
        result, elapsed_time = linearSearch.exists(username)
        self.assertFalse(result)  # It should return False for a non-existing username
        self.assertGreater(elapsed_time, 0)  # Ensure some time was taken

    def test_binary_exists_username_found(self):
        """
        Test case for the `BinarySearch` class when the username exists in the dataset.

        This test verifies that the `exists` method of the `BinarySearch` class correctly identifies
        if a given username exists in the list of usernames. The test checks for:
        - Returning `True` when the username is found.
        - Ensuring that the execution time is measured correctly.

        Steps:
        1. A list of sample usernames is created.
        2. The `exists` method is called with a username that is in the list.
        3. The test asserts that the result is `True`, indicating the username was found.
        4. The test asserts that the execution time is greater than 0.

        Asserts:
        - True if the username is found.
        - The elapsed time of the method execution is greater than 0.
        """
        usernames = ['user1', 'user2', 'user3']
        username = 'user2'
        binarySearch = BinarySearch(usernames)
        result, elapsed_time = binarySearch.exists(username)
        self.assertTrue(result)  # It should return True for an existing username
        self.assertGreater(elapsed_time, 0)  # Ensure some time was taken

    def test_binary_exists_username_not_found(self):
        """
        Test case for the `BinarySearch` class when the username does not exist in the dataset.

        This test verifies that the `exists` method of the `BinarySearch` class correctly identifies
        if a given username is not in the list of usernames. The test checks for:
        - Returning `False` when the username is not found.
        - Ensuring that the execution time is measured correctly.

        Steps:
        1. A list of sample usernames is created.
        2. The `exists` method is called with a username that is not in the list.
        3. The test asserts that the result is `False`, indicating the username was not found.
        4. The test asserts that the execution time is greater than 0.

        Asserts:
        - False if the username is not found.
        - The elapsed time of the method execution is greater than 0.
        """
        usernames = ['user1', 'user2', 'user3']
        username = 'user4'
        binarySearch = BinarySearch(usernames)
        result, elapsed_time = binarySearch.exists(username)
        self.assertFalse(result)  # It should return False for a non-existing username
        self.assertGreater(elapsed_time, 0)  # Ensure some time was taken