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

if __name__ == "__main__":
    pq = MyQueue()

    pq.enqueue({
        'company': 'Wal mart',
        'timestamp': '15 apr, 11.01 AM',
        'price': 131.10
    })
    pq.enqueue({
        'company': 'Wal mart',
        'timestamp': '15 apr, 11.02 AM',
        'price': 132
    })
    pq.enqueue({
        'company': 'Wal mart',
        'timestamp': '15 apr, 11.03 AM',
        'price': 135
    })

    print(pq.dequeue())