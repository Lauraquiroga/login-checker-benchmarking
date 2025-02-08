import unittest
import math
from src.cuckoo_filter import CuckooFilter

class TestCuckoo(unittest.TestCase):

    def test_initialization(self):
        """
        Test initialization: capacity and fingerprint size calculations
        """
        filter = CuckooFilter(data_size=100, fp_prob=0.01, b=4, load_factor=0.75)
        self.assertEqual(filter.capacity, math.ceil(100 / (0.75 * 4)))
        self.assertEqual(filter.fingerprint_size, math.ceil(math.log2(2 * 4 / 0.01) / 8))
                                                            
    def test_exists_items_added(self):
        """
        Test if an item that is added to the Cuckoo filter it is found correctly
        """
        usernames = ['user1', 'user2', 'user3']
        filter = CuckooFilter(len(usernames), 0.1)  # 10% fpp

        # Add items to the Cuckoo filter
        filter.initialize_with_dataset(usernames)

        # Check for existance: Since there are no False Negatives, all results must be True
        for username in usernames:
            result, elapsed_time = filter.exists(username)
            self.assertTrue(result)
            self.assertGreater(elapsed_time, 0)  # Ensure some time was taken

    def test_insertion_and_existence(self):
        """
        Test using single-item insertion
        """
        filter = CuckooFilter(data_size=100, fp_prob=0.01)
        logins = ["user1", "user2", "user3"]
        for login in logins:
            self.assertIsNotNone(filter.insert(login))
        for login in logins:
            result, elapsed_time = filter.exists(login)
            self.assertTrue(result)
            self.assertGreater(elapsed_time, 0)  # Ensure some time was taken

    def test_full_filter(self):
        """
        Test that filter handles max evictions correctly
        """
        filter = CuckooFilter(data_size=10, fp_prob=0.01, max_evictions=20)
        logins = [f"user{i}" for i in range(30)]  # More items than the filter's capacity
        try:
            filter.initialize_with_dataset(logins)
        except Exception as e:
            self.assertEqual(str(e), 'Filter is full')

    def test_edge_case_empty_filter(self):
        """
        Test behavior with an empty Cuckoo filter.

        False result always expected (No elements inserted -> no probability of False Positive = 0)
        """
        bf = CuckooFilter(10, 0.01)
        result, _ = bf.exists("non_existent_user")
        self.assertFalse(result, "Expected 'non_existent_user' to not be found in the empty filter.")