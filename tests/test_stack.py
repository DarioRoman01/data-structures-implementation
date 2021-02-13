"""Stack tests."""

# Testing
import unittest

# Data structure
from stacks import Stack

class TestStack(unittest.TestCase):
    """Stack test case."""

    def setUp(self):
        """Set up test case."""
        self.stack = Stack()
        self.stack.push('hello')

    def test_push_and_peek_method(self):
        """Test push and peek method."""
        s = self.stack
        self.assertIsNotNone(s.peek())
        self.assertEqual(s.size(), 1)

    def test_pop_and_is_empty_method(self):
        """Test pop mehotd and is empty"""
        s = self.stack
        self.assertEqual('hello', s.pop())
        self.assertTrue(s.is_empty())

    def test_size_method(self):
        """Test .size() method."""
        s = self.stack
        self.assertEqual(s.size(), 1)
