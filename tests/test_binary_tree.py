"""General tree tests."""

# Testing
import unittest

# Binary tree
from trees import BinarySearchTreeNode
from trees import build_tree

class TestGeneralTree(unittest.TestCase):
    """General tree test case."""

    def setUp(self):
        """Test case set up."""
        numbers = [17, 4, 1, 20, 9, 23, 18, 34, 18, 4]
        self.tree = build_tree(numbers)

    def test_in_order_transversal(self):
        """Test in order transversal method."""
        t = self.tree
        expected = [1, 4, 9, 17, 18, 20, 23, 34]
        result = t.in_order_transversal()
        self.assertEqual(result, expected)

    def test_post_order_transversal(self):
        """Test post order transversal method."""
        t = self.tree
        expected = [1, 4, 9, 18, 20, 23, 34, 17]
        result = t.post_order_transversal()
        self.assertEqual(result, expected)

    def test_pre_order_transversal(self):
        """Test pre order transversal method."""
        t = self.tree
        expected = [17, 1, 4, 9, 18, 20, 23, 34] 
        result = t.pre_order_transversal()
        self.assertEqual(result, expected)

    def test_find_max(self):
        """Test find max method."""
        t = self.tree
        expected = 34 # is the max value
        result = t.find_max()
        self.assertEqual(result, expected)

    def test_find_min(self):
        t = self.tree
        expected = 1 # is the min value
        result = t.find_min()
        self.assertEqual(result, expected)

    def test_calculate_sum(self):
        """Test calculate sum method."""
        t = self.tree
        expected = 126
        result = t.calculate_sum()
        self.assertEqual(result, expected)

    def test_search(self):
        """Test search method return true if the element is find else false."""
        t = self.tree
        self.assertTrue(t.search(20))
        self.assertFalse(t.search(98))

    def test_delete(self):
        """Test delete method."""
        t = self.tree
        t.delete(4)
        expected = [1, 9, 17, 18, 20, 23, 34]
        result = t.in_order_transversal()
        self.assertEqual(result, expected)
        self.assertFalse(t.search(4))
