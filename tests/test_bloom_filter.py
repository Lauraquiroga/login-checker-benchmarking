import unittest
import random
from src.bloom_filter import BloomFilter

class TestBloom(unittest.TestCase):
    """
    Unit test class for the `BloomFilter` class, using Python's built-in unittest framework.
    """

    def test_exists_item_added(self):
        """
        Test if an item that is added to the Bloom filter it is found correctly
        """
        usernames = ['user1', 'user2', 'user3']
        bf = BloomFilter(len(usernames), 0.1)  # 10% fpp

        # Add items to the Bloom filter
        bf.initialize_with_dataset(usernames)

        # Check for existance: Since there are no False Negatives, all results must be True
        for username in usernames:
            result, elapsed_time = bf.exists(username)
            self.assertTrue(result)
            self.assertGreater(elapsed_time, 0)  # Ensure some time was taken

    def test_false_positive_rate(self):
        """ 
        Test to check that the false positive rate is within an acceptable range
        """
        usernames = [f'user_{x}' for x in range(100)]
        fpp = 0.1 # 10% fpp
        acceptable_fp_range = [0.065, 0.135]
        bf = BloomFilter(len(usernames), fpp)

        # Add items to the Bloom filter
        bf.initialize_with_dataset(usernames)

        false_positives = 0
        total_checks = 1000

        # Perform 1000 checks on items not in the Bloom filter to check false positives
        for _ in range(total_checks):
            non_existing_username = f'user{random.randint(6, 1000)}'  # Generate random non-existing username
            result, _ = bf.exists(non_existing_username)
            if result:
                false_positives += 1

        # Check if the false positive rate is within the expected range (i.e. at most given fpp)
        false_positive_rate = false_positives / total_checks
        self.assertGreaterEqual(false_positive_rate, acceptable_fp_range[0],
                                f"False positive rate too low: {false_positive_rate}")
        self.assertLessEqual(false_positive_rate, acceptable_fp_range[1],
                             f"False positive rate too high: {false_positive_rate}")
        
    def test_edge_case_empty_filter(self):
        """
        Test behavior with an empty Bloom filter.

        False result always expected (No elements inserted -> no probability of False Positive = 0)
        """
        bf = BloomFilter(10, 0.1) # 10% fpp
        result, _ = bf.exists("non_existent_user")
        self.assertFalse(result, "Expected 'non_existent_user' to not be found in the empty filter.")