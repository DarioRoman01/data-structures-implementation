"""Queue implentation."""

# Utils
from collections import deque

class MyQueue:
    """Queue class."""

    def __init__(self):
        self.buffer = deque()

    def enqueue(self, val):
        """Add element at begining of the queue."""
        self.buffer.appendleft(val)

    def dequeue(self):
        """Remove the last element of the queue and return it."""
        return self.buffer.pop()

    def is_empty(self):
        """Return true if the list is empty."""
        return len(self.buffer)==0

    def size(self):
        """Return the size of the queue."""
        return len(self.buffer)

    def front(self):
        """return the front element in the queue"""
        return self.buffer[-1]