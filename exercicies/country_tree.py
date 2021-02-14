# Tree
from trees import TreeNode

def build_location_tree():
    root = TreeNode('Global')

    usa = TreeNode('USA')
    chl = TreeNode('Chile')

    # Build New jersie tree
    nej = TreeNode('New Jersie')
    nej.add_child(TreeNode('Princeton'))
    nej.add_child(TreeNode('Treton'))
    # Build california tree
    cal = TreeNode('California')
    cal.add_child(TreeNode('San Francisco'))
    cal.add_child(TreeNode('Mountain view'))
    cal.add_child(TreeNode('Palo Alto'))
    # Finish usa tree
    usa.add_child(nej)
    usa.add_child(cal)
    
    # Build Region Metropolitana region
    rm = TreeNode('Region Metropolitana')
    rm.add_child(TreeNode('Santiago'))
    rm.add_child(TreeNode('Maipu'))

    # Build Punta Arenas tree
    mas = TreeNode('Magallanes')
    mas.add_child(TreeNode('Punta Arenas'))
    mas.add_child(TreeNode('Puerto Natales'))

    # Finish Chile Tree
    chl.add_child(rm)
    chl.add_child(mas)

    # Finish all tree
    root.add_child(chl)
    root.add_child(usa)

    return root


if __name__ == "__main__":
    root = build_location_tree()
    root.print_tree(1)