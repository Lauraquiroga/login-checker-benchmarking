import unittest
from src.cuckoo_filter import CuckooFilter

class TestCuckoo(unittest.TestCase):

    def test_exists_item_added(self):
        """
        Test if an item that is added to the Bloom filter it is found correctly
        """
        usernames = ['user1', 'user2', 'user3']
        cf = CuckooFilter(len(usernames), 0.1)  # 10% fpp

        # Add items to the Cuckoo filter
        cf.initialize_with_dataset(usernames)

        # Check for existance: Since there are no False Negatives, all results must be True
        for username in usernames:
            result, elapsed_time = cf.exists(username)
            self.assertTrue(result)
            self.assertGreater(elapsed_time, 0)  # Ensure some time was taken