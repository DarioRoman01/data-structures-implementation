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
        list_tree = self.in_order_transversal()
        min_value = min(list_tree)
        return min_value

    def find_max(self):
        """Get the item max value of the tree."""
        list_tree = self.in_order_transversal()
        max_value = max(list_tree)
        return max_value

    def calculate_sum(self):
        """Return the sum of all the elements in the tree."""
        list_tree = self.in_order_transversal()
        total = sum(list_tree)
        return total


def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])
    
    for element in elements[1:]:
        root.add_child(element)

    return root

if __name__ == "__main__":
    numbers = [17, 4, 1, 20, 9, 23, 18, 34, 18, 4]
    numbers_tree = build_tree(numbers)

    countries = ['India', 'Pakistan', 'Germany', 'USA', 'China', 'India', 'UK', 'USA']
    country_tree = build_tree(countries)

    # print('Is UK in the list? ', country_tree.search('UK'))
    # print('Sweden is in the list? ', country_tree.search('Sweden'))
    # print(country_tree.in_order_transversal())
    print(numbers_tree.in_order_transversal())
    print(numbers_tree.post_order_transversal())
    print(numbers_tree.pre_order_transversal())
    print(numbers_tree.find_max())
    print(numbers_tree.calculate_sum())