"""Stack implementation using deque class"""

# Utilities
from collections import deque

class Stack:
    """Stack class."""

    def __init__(self):
        self.container = deque()

    def push(self, value):
        """Add item to the top of the stack"""
        self.container.append(value)
    
    def pop(self):
        """Delete the top item of the stack."""
        return self.container.pop()

    def peek(self):
        """Get the top item of the stack."""
        return self.container[-1]

    def is_empty(self):
        """Check that the stack is empty."""
        return len(self.container)==0

    def size(self):
        """Return the size of the stack."""
        return len(self.container)
