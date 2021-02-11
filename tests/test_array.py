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

    def test_delete_element(self):
        """Test deletions of elements"""
        array = self.array
        array.push('dario')
        array.push('jose')
        array.pop()
        self.assertNotEqual(array.length, 2)



if __name__ == "__main__":
    unittest.main()
        

