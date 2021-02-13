"""Stack implementation."""

# Utilities
from collections import deque

class Stack:
    """Stack class."""

    def __init__(self):
        self.container = deque()

    def push(self, value):
        self.container.append(value)
    
    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def is_empty(self):
        return len(self.container)==0

    def size(self):
        return len(self.container)
