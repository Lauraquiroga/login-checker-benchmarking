import unittest
from src.cuckoo_bucket import Bucket

class TestBucket(unittest.TestCase):

    def test_initialization(self):
        """
        Test Cuckoo Filter's Bucket initialization
        """
        bucket = Bucket(size=4)
        self.assertEqual(bucket.size, 4)
        self.assertEqual(len(bucket.b), 0)

    def test_insertion(self):
        """
        Test Cuckoo Filter's Bucket insertion method
        """
        bucket = Bucket(size=4)
        self.assertTrue(bucket.insert("fp1"))
        self.assertTrue(bucket.insert("fp2"))
        self.assertTrue(bucket.insert("fp3"))
        self.assertTrue(bucket.insert("fp4"))
        self.assertFalse(bucket.insert("fp5"))  # Bucket should be full now

    def test_contains(self):
        """
        Test Cuckoo Filter's Bucket contains method
        """
        bucket = Bucket(size=4)
        bucket.insert("fp1")
        self.assertTrue(bucket.contains("fp1"))
        self.assertFalse(bucket.contains("fp2"))

    def test_deletion(self):
        """
        Test Cuckoo Filter's Bucket delete method
        """
        bucket = Bucket(size=4)
        bucket.insert("fp1")
        self.assertTrue(bucket.delete("fp1"))
        self.assertFalse(bucket.delete("fp2"))
        self.assertFalse(bucket.contains("fp1"))

    def test_swap(self):
        """
        Test Cuckoo Filter's Bucket swap method
        """
        bucket = Bucket(size=4)
        bucket.insert("fp1")
        bucket.insert("fp2")
        original_fp = bucket.b[0]
        swapped_fp = bucket.swap("fp3")
        self.assertEqual(swapped_fp, original_fp)
        self.assertIn("fp3", bucket.b)
        self.assertNotIn(original_fp, bucket.b)

    def test_is_full(self):
        """
        Test Cuckoo Filter's Bucket is full
        """
        bucket = Bucket(size=4)
        self.assertFalse(bucket.is_full())
        bucket.insert("fp1")
        bucket.insert("fp2")
        bucket.insert("fp3")
        bucket.insert("fp4")
        self.assertTrue(bucket.is_full())