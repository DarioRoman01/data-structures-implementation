class Node:
    def __init__(self, data=None, next=None):
        """Constructor"""
        self.data = data
        self.next = next
        

class LinkedList:
    def __init__(self):
        """Constructor."""
        self.head = None

    def insert_at_begining(self, data):
        """Insert element in first position."""
        node = Node(data, self.head)
        self.head = node

    def print(self):
        """Print the list."""
        if self.head is None:
            print('Linked list is empty')
            return

        itr = self.head
        llstr = ''

        while itr:
            llstr += str(itr.data) + '--> '
            itr = itr.next
        print(llstr)

    def insert_at_end(self, data):
        """Insert element at last position."""
        if self.head is None:
            self.head = Node(data, None)
            return
        
        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    def insert_values(self, data_list):
        """Insert a list of elements."""
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):
        """get the length of the list."""
        count = 0 
        itr = self.head

        while itr:
            count += 1
            itr = itr.next

        return count

    def remove_at(self, index):
        """Remove element by index."""
        if index < 0 or index >= self.get_length():
            raise Exception('Invalid index')
        
        if index == 0:
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break

            itr = itr.next
            count += 1

    def insert_at(self, data, index):
        """Insert element by index."""
        if index < 0 or index >= self.get_length():
            raise Exception('Invalid index')

        if index == 0:
            self.insert_at_begining(data)
            return

        count = 0
        itr = self.head

        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break

            itr = itr.next
            count += 1

    def insert_after_value(self, data_after, data_to_insert):
        """Insert a element after a given element of the list.""" 
        itr = self.head
        count = 0
        while itr:
            if itr.data == data_after:
                self.insert_at(data_to_insert, count)
                break

            itr = itr.next
            count += 1

    def remove_by_value(self, data):
        """Remove element by value."""
        itr = self.head
        count = 0
        while itr:
            if itr.data == data:
                self.remove_at(count)
                break

            itr = itr.next
            count += 1

if __name__ == "__main__":
    """Testing the implementation."""
    ll = LinkedList()
    ll.insert_values(['dario', 'pedro', 'juan', 'diego', 'owo'])
    ll.print()
    ll.insert_at('pablo', 0)
    ll.print()
    ll.insert_at('vicente', 2)
    ll.print()
    ll.insert_after_value('dario', 'kiba')
    ll.print()
    ll.remove_by_value('juan')
    ll.print()
