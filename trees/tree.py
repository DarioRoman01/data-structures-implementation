class TreeNode:
    def __init__(self, data):
        """Constructor."""
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        """Add a children to the node."""
        child.parent = self
        self.children.append(child)


    def get_level(self):
        """Get the level of the instance based on his parents"""
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def print_tree(self, lvl):
        if self.get_level() > lvl:
            return
        spaces = ' ' * self.get_level() * 5
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + self.data)

        if self.children:
            for child in self.children:
                child.print_tree(lvl)