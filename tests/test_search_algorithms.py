import unittest
from src.linear_search import LinearSearch
from src.binary_search import BinarySearch

class TestSearchAlgorithms(unittest.TestCase):

    def test_linear_exists_username_found(self):
        usernames = ['user1', 'user2', 'user3']
        username = 'user2'
        result, elapsed_time = LinearSearch.exists(usernames, username)
        self.assertTrue(result)  # It should return True for an existing username
        self.assertGreater(elapsed_time, 0)  # Ensure some time was taken

    def test_linear_exists_username_not_found(self):
        usernames = ['user1', 'user2', 'user3']
        username = 'user4'
        result, elapsed_time = LinearSearch.exists(usernames, username)
        self.assertFalse(result)  # It should return False for a non-existing username
        self.assertGreater(elapsed_time, 0)  # Ensure some time was taken

    def test_binary_exists_username_found(self):
        usernames = ['user1', 'user2', 'user3']
        username = 'user2'
        binarySearch = BinarySearch(usernames, username)
        result, elapsed_time = binarySearch.exists()
        self.assertTrue(result)  # It should return True for an existing username
        self.assertGreater(elapsed_time, 0)  # Ensure some time was taken

    def test_binary_exists_username_not_found(self):
        usernames = ['user1', 'user2', 'user3']
        username = 'user4'
        binarySearch = BinarySearch(usernames, username)
        result, elapsed_time = binarySearch.exists()
        self.assertFalse(result)  # It should return False for a non-existing username
        self.assertGreater(elapsed_time, 0)  # Ensure some time was taken