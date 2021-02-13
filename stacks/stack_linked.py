"""Stack implementation using linked lists."""

class StackNode:
    """Stack node class."""

    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class Stack:
    """Stack class."""

    def __init__(self):
        self.head = None

    def is_empty(self):
        """Check that the stack is empty."""
        return True if self.head is None else False

    def push(self, data):
        """Add item to the top of the stack"""
        if self.head is None:
            node = StackNode(data, self.head, None)
            self.head = node

        else:    
            node = StackNode(data, self.head, None)
            self.head.prev = node
            self.head = node
        
        return self.head.data   

    
    
    def pop(self):
        """Delete the top item of the stack and return it"""
        h = self.head
        if self.is_empty():
            return 'The list is empty'

        self.head = h.next
        popped = h.data
        return popped

    def peek(self):
        """Get the top item of the stack."""
        return self.head.data     

    def size(self):
        """Return the size of the stack."""
        count = 0
        itr = self.head

        while itr:
            count += 1
            itr = itr.next

        return count

if __name__ == "__main__":
    s = Stack()
    print(s.push('dario'))
    print(s.push('jose'))
    print(s.push('diego'))
    # print(s.peek())
    print(s.pop())
    print(s.size())

