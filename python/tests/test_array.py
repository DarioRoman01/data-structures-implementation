"""Array tests."""

# Testing
import unittest

# Data structures
from arrays import MyArray

class TestArray(unittest.TestCase):
    """Array testing."""

    def setUp(self):
        self.array = MyArray()
        

    def test_add_element(self):
        """test that an element is added to the array."""
        array = self.array
        array.push('dario')
        self.assertIsNotNone(array.get(0))


    def test_pop_element(self):
        """Test deletions of elements"""
        array = self.array
        array.push('dario')
        array.push('jose')
        array.pop()
        self.assertNotEqual(array.length, 2)


    def test_unshift_elemnent(self):
        """Test unshif element in the array."""
        array = self.array
        array.push('dario')
        array.push('jose')
        array.unshift('willy')
        self.assertEqual(array.get(0), 'willy')


    def test_remove_element(self):
        """Test remove element by index."""
        array = self.array
        array.push('dario')
        array.push('jose')
        array.push('willy')
        array.remove(1)
        self.assertNotEqual(array.get(1), 'jose')


    def test_shift_element(self):
        """Test delete element at first position."""
        array = self.array
        array.push('dario')
        array.push('jose')
        array.push('willy')
        array.shift()
        self.assertNotEqual(array.get(0), 'dario')


if __name__ == "__main__":
    unittest.main()