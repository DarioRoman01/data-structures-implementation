"""Hash table tests."""

# Testing
import unittest

# Data structures
from hash_tables import HashTable

class TestHashTable(unittest.TestCase):
    """Hash table test case."""

    def setUp(self):
        """set up test case."""
        self.hash_table = HashTable()
        self.hash_table["march 6"] = 130
        self.hash_table["march 17"] = 204
        self.hash_table["march 24"] = 210
        self.hash_table["march 30"] = 207

    def test_add_item(self):
        """Test add item to the table"""
        ht = self.hash_table
        self.assertIsNotNone(ht['march 6'])

    def test_get_method(self):
        """Test get method."""
        ht = self.hash_table
       
        self.assertEqual(ht['march 6'], ht.get('march 6'))

    def test_remove_item(self):
        """Test remove item from the table."""
        ht = self.hash_table
       
        del ht['march 6']
        self.assertIsNone(ht['march 6'])

    def test_colission_handler(self):
        """Test that in one position can be more than one element."""
        ht = self.hash_table
        ht["april 4"] = 210
        ht["april 10"] = 250
        ht["april 13"] = 230
        self.assertEqual(len(ht.arr[9]), 2)

    def test_values_method(self):
        """test .values() method."""
        ht = self.hash_table
        self.assertIn(ht.get('march 6'), ht.values())

    def test_keys_method(self):
        """Test .keys() mehtod. should return all the keys"""
        ht = self.hash_table
        self.assertIn('march 24', ht.keys())
        self.assertEqual(len(ht.keys()), 4)

    def test_items_method(self):
        """Test .items() method. should reutrn a list 
        that contains all the items of the table"""
        ht = self.hash_table
        self.assertIn(('march 24', 210), ht.items())

    def test_from_keys_method(self):
        """Test .from_keys() method should return a dict"""
        ht = self.hash_table
        self.assertEqual({'march 17': 204}, ht.from_keys('march 17'))

    def test_pop_method(self):
        """Test .pop() method, should return false."""
        ht = self.hash_table
        self.assertIsNone(ht.pop('march 6'))
        self.assertEqual(len(ht.items()), 3)

if __name__ == "__main__":
    unittest.main()