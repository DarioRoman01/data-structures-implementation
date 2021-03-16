class Node:
    def __init__(self, data=None, next=None, prev=None):
        """Constructor"""
        self.data = data
        self.next = next
        self.prev = prev


class DoubleLinkList:
    def __init__(self):
        self.head = None

    def print_forward(self):
        """Print the list in forward format."""
        if self.head is None:
            print('Linked list is empty')
            return

        itr = self.head
        llstr = ''

        while itr:
            llstr += str(itr.data) + '-->'
            itr = itr.next
        
        print(llstr)

    def print_backward(self):
        """Print the list in backward format."""
        if self.head is None:
            print('Linked list is empty')
            return

        last_node = self.get_last_node()
        itr = last_node
        llstr = ''

        while itr:
            llstr += itr.data + '-->'
            itr = itr.prev

        print(llstr) 


    def get_last_node(self):
        """Get the last element of the list."""
        itr = self.head

        while itr.next:
            itr = itr.next

        return itr

    def get_length(self):
        """Get the length of the list."""
        count = 0 
        itr = self.head

        while itr:
            count += 1
            itr = itr.next

        return count

    def insert_at_begining(self, data):
        """Insert element at first position."""
        if self.head is None:
            node = Node(data, self.head, None)
            self.head = node
        else:
            node = Node(data, self.head, None)
            self.head.prev = node
            self.head = node


    def insert_at_end(self, data):
        """Insert a element at the end of the list."""
        if self.head is None:
            self.head = Node(data, None, None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None, itr)

    def insert_at(self, index, data):
        """Insert element in a given index of the list."""
        if index < 0 or index >= self.get_length():
            raise Exception('Invalid index')

        if index == 0:
            self.insert_at_begining(data)

        count = 0
        itr = self.head

        while itr:
            if count == index - 1:
                node = Node(data, itr.next, itr)
                if node.next:
                    itr.next.prev = node
                itr.next = node
                break
            
            itr = itr.next
            count += 1


    def remove_at(self, index):
        """Remove element by index."""
        if index < 0 or index >= self.get_length():
            raise Exception('Invalid index')

        if index == 0:
            self.head = self.head.next
            self.head.prev = None
            return

        count = 0
        itr = self.head

        while itr:
            if count == index:
                itr.prev.next = itr.next
                if itr.next:
                    itr.next.prev = itr.prev
                break
            
            itr = itr.next
            count += 1


    def insert_values(self, data_list):
        """Insert a list of elements."""
        for data in data_list:
            self.insert_at_end(data)


    def insert_after_value(self, data_after, data_to_insert):
        """Insert a element after a given element of the list.""" 
        itr = self.head
        count = 0
        while itr:
            if itr.data == data_after:
                self.insert_at(count + 1, data_to_insert)
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

    def get_by_value(self, data):
        """Get elements by value"""
        itr = self.head
        while itr:
            if itr.data == data:
                return itr
            
            itr = itr.next

    def get_by_index(self, index):
        """Get elements by index."""
        itr = self.head
        count = 0
        while itr:
            if count == index:
                return itr
            
            itr = itr.next
            count += 1