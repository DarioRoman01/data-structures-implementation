"""Binary tree implementation."""

class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        """Add a child to the tree node."""
        if data == self.data:
            return # node already exists

        if data < self.data:
            # Add data to the left sub tree
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)

        else:
            # Add data to the right sub tree
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)

    
    def in_order_transversal(self):
        elements = []

        # Get left tree
        if self.left:
            elements += self.left.in_order_transversal()

        # Get the base node
        elements.append(self.data)

        # Get right tree
        if self.right:
            elements += self.right.in_order_transversal()
        
        return elements

    def pre_order_transversal(self):
        elements = []

        # Get the base node
        elements.append(self.data)

        # Get left tree
        if self.left:
            elements += self.left.in_order_transversal()

        # Get right tree
        if self.right:
            elements += self.right.in_order_transversal()
        
        return elements

    def post_order_transversal(self):
        elements = []
        
        # Get left tree
        if self.left:
            elements += self.left.in_order_transversal()

        # Get right tree
        if self.right:
            elements += self.right.in_order_transversal()
        
        # Get the base node
        elements.append(self.data)

        return elements

    def search(self, value):
        """Search for a value in the tree."""
        if self.data == value:
            return True
        
        # Check the left tree
        if value < self.data:
            if self.left:
                return self.left.search(value)
            else:
                return False

        # Check the right tree
        if value > self.data:
            if self.right:
                return self.right.search(value)
            else: 
                return False
    
    def find_min(self):
        """Get the min value of the tree."""
        if self.left is None:
            return self.data
        else:
            list_tree = self.in_order_transversal()
            min_value = list_tree[0]
            return min_value

    def find_max(self):
        """Get the item max value of the tree."""
        if self.right is None:
            return self.data
        else:
            list_tree = self.in_order_transversal()
            max_value = list_tree[-1]
            return max_value

    def calculate_sum(self):
        """Return the sum of all the elements in the tree."""
        if self.left is None:
            return self.data
        elif self.right is None:
            return self.data
        else:
            list_tree = self.in_order_transversal()
            total = sum(list_tree)
            return total

    def delete(self, value):
        """Delete a specified item."""
        if value < self.data:
            if self.left:
                self.left = self.left.delete(value)

        elif value > self.data:
            if self.right:
                self.right = self.right.delete(value)

        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left

            min_val = self.right.find_max()
            self.data = min_val
            self.right = self.right.delete(min_val)

        return self

    
def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])
    
    for element in elements[1:]:
        root.add_child(element)

    return root
