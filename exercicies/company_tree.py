"""General tree implementation. for a fictitious company
Should return a graphic representation of the tree."""

class TreeNode:
    def __init__(self, name, job):
        """Constructor."""
        self.name = name
        self.job = job 
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

    def print_tree_by_name(self):
        """Print tree with the names."""
        spaces = ' ' * self.get_level() * 5
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + self.name)

        if len(self.children) > 0:                
            for child in self.children:
                child.print_tree_by_name()

    def print_tree_by_job(self):
        """Print tree with the jobs."""
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + self.job)

        if len(self.children) > 0:                
            for child in self.children:
                child.print_tree_by_job()

    def print_full_tree(self):
        """Print tree using name and job."""
        spaces = ' ' * self.get_level() * 7
        prefix = spaces + "|__" if self.parent else ""
        print(f'{prefix}{self.name}({self.job})')

        if len(self.children) > 0:                
            for child in self.children:
                child.print_full_tree()


def build_management_tree():
    root = TreeNode('Nilupul', 'CEO')

    # Make the tree for the CTO
    cto = TreeNode('Chinmay', 'CTO')
    inf_head = TreeNode('Vishaw', 'Infrastructure head')
    inf_head.add_child(TreeNode('Dhaval', 'Cloud Manager'))
    inf_head.add_child(TreeNode('Abhijit', 'App Manager'))
    app_head = TreeNode('Aamir', 'Application head')
    cto.add_child(inf_head)
    cto.add_child(app_head)

    # Make the tree for HR Head
    hr_head = TreeNode('Geals', 'HR Head')
    hr_head.add_child(TreeNode('Peter', 'Recruitment Manager'))
    hr_head.add_child(TreeNode('Waqas', 'Policy Manager'))

    # Finish tree conecting to the CEO
    root.add_child(cto)
    root.add_child(hr_head)

    return root


if __name__ == "__main__":
    root = build_management_tree()
    root.print_full_tree()

    