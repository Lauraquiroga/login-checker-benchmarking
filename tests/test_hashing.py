import unittest
from src.hashing import Hashing

class TestHashing(unittest.TestCase):

    def test_exists_username_found(self):
        usernames = ['user1', 'user2', 'user3']
        username = 'user2'
        result, elapsed_time = Hashing.exists(usernames, username)
        self.assertTrue(result)  # It should return True for an existing username
        self.assertGreater(elapsed_time, 0)  # Ensure some time was taken

    def test_exists_username_not_found(self):
        usernames = ['user1', 'user2', 'user3']
        username = 'user4'
        result, elapsed_time = Hashing.exists(usernames, username)
        self.assertFalse(result)  # It should return False for a non-existing username
        self.assertGreater(elapsed_time, 0)  # Ensure some time was taken
