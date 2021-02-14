"""Queues tests."""

# Testing
import unittest

# Queues
from queues import MyQueue

class TestQueue(unittest.TestCase):
    """Queue test case."""

    def setUp(self):
        """Test case set up."""
        self.queue = MyQueue()

        self.queue.enqueue({
            'company': 'Wal mart',
            'timestamp': '15 apr, 11.01 AM',
            'price': 131.10
        })
        self.queue.enqueue({
            'company': 'Wal mart',
            'timestamp': '15 apr, 11.02 AM',
            'price': 132
        })
        self.queue.enqueue({
            'company': 'Wal mart',
            'timestamp': '15 apr, 11.03 AM',
            'price': 135
        })

    def test_enqueue_method(self):
        """Test that are elements in the queue and .is_empty() method"""
        q = self.queue
        self.assertFalse(q.is_empty())

    def test_front_method(self):
        """Test .front() method comparing front with and object."""
        q = self.queue

        object_ = {
        'company': 'Wal mart',
        'timestamp': '15 apr, 11.01 AM',
        'price': 131.10
        }

        self.assertEqual(q.front(), object_)

    def test_dequeue_method(self):
        q = self.queue

        object_ = {
        'company': 'Wal mart',
        'timestamp': '15 apr, 11.01 AM',
        'price': 131.10
        }

        self.assertEqual(q.dequeue(), object_)
        self.assertNotIn(object_, q.buffer)

    def test_size_method(self):
        q = self.queue
        self.assertEqual(q.size(), 3)
