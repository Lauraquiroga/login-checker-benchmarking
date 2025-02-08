import unittest
from src.hashing import Hashing

class TestHashing(unittest.TestCase):
    """
    Unit test class for the `Hashing` class, using Python's built-in unittest framework.
    """

    def test_exists_username_found(self):
        """
        Test case to check if a username that exists in the dataset returns True.

        This test verifies that when a username is found in the list of usernames, 
        the `exists` method returns `True`. It also checks that the execution time is measured correctly.
        
        Steps:
        1. A list of sample usernames is created.
        2. The `exists` method is called with a username that is in the list.
        3. The test asserts that the result is `True`, indicating the username was found.
        4. The test asserts that some time was taken to execute the method.
        
        Asserts:
        - True if the username exists in the dataset.
        - The elapsed time of the method execution is greater than 0.
        """
        usernames = ['user1', 'user2', 'user3']
        username = 'user2'
        hashing = Hashing(usernames)
        result, elapsed_time = hashing.exists(username)
        self.assertTrue(result)  # It should return True for an existing username
        self.assertGreater(elapsed_time, 0)  # Ensure some time was taken

    def test_exists_username_not_found(self):
        """
        Test case to check if a username that does not exist in the dataset returns False.

        This test verifies that when a username is not found in the list of usernames, 
        the `exists` method returns `False`. It also checks that the execution time is measured correctly.
        
        Steps:
        1. A list of sample usernames is created.
        2. The `exists` method is called with a username that is not in the list.
        3. The test asserts that the result is `False`, indicating the username was not found.
        4. The test asserts that some time was taken to execute the method.
        
        Asserts:
        - False if the username does not exist in the dataset.
        - The elapsed time of the method execution is greater than 0.
        """
        usernames = ['user1', 'user2', 'user3']
        username = 'user4'
        hashing = Hashing(usernames)
        result, elapsed_time = hashing.exists(username)
        self.assertFalse(result)  # It should return False for a non-existing username
        self.assertGreater(elapsed_time, 0)  # Ensure some time was taken