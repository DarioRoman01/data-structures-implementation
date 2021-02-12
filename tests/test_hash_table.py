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

    def test_add_item(self):
        """Test add item to the table and get method."""
        ht = self.hash_table
        ht['march 6'] = 130
        self.assertIsNotNone(ht['march 6'])

    def test_remove_item(self):
        """Test remove item from the table."""
        ht = self.hash_table
        ht['march 6'] = 130
        ht['december 24'] = 235
        ht['march 19'] = 190
        del ht['march 6']
        self.assertIsNone(ht['march 6'])