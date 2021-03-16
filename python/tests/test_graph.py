"""Grahp tests."""

# Testing
import unittest

# Graph
from graphs import Graph

class TestGraph(unittest.TestCase):
    """Graph test case."""

    def setUp(self):
        """Test case set up."""
        routes = [
        ('Mumbai', 'Paris'),
        ('Mumbai', 'Dubai'),
        ('Paris', 'Dubai'),
        ('Paris', 'New York'),
        ('Dubai', 'New York'),
        ('New York', 'Toronto'),
        ]
        self.graph = Graph(routes)

    def test_get_paths(self):
        g = self.graph
        start = 'Paris'
        end = 'Toronto'
        expected = [['Paris', 'Dubai', 'New York', 'Toronto'], ['Paris', 'New York', 'Toronto']]
        results = g.get_paths(start, end)
        self.assertEqual(results, expected)

    def test_get_short_path(self):
        g = self.graph
        start = 'Mumbai'
        end = 'Toronto'
        expected = ['Mumbai', 'Paris', 'New York', 'Toronto']
        result = g.get_short_path(start, end)

