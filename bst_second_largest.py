def find_largest(root_node):
    """Find largest node in binary search tree."""

    if root_node is None:
        raise Exception('Tree must have at least 1 node.')
    if root_node.right is not None:
        return find_largest(root_node.right)

    return root_node.value


def find_second_largest(root_node):
    """Find second largest node in BST in O(h) time and space."""
    if root_node is None or (root_node.left is None and root_node.right is None):
        raise Exception('Tree must have at least two nodes.')

    # if currently at largest and largest has a left subtree, 2nd largest
    # is largest in said subtree
    if root_node.left and not root_node.right:
        return find_largest(root_node.left)

    # if at parent of largest and largest has no subtree, 2nd largest must be current node
    if root_node.right and not root_node.right.left and not root_node.right.right:
        return root_node.value

    # otherwise, step right
    return find_second_largest(root_node.right)


def find_largest_improved(root_node):
    current = root_node
    while current:
        if not current.right:
            return current.value
        current = current.right

def find_second_largest_improved(root_node):
    if root_node is None or(root_node.left is None and root_node.right is None):
        raise Exception('Tree must have at least 2 nodes.')

    current = root_node

    while current:
        # if current is largest and has left subtree, 
        # 2nd largest is largest in that subtree
        if current.left and not current.right:
            return find_largest_improved(current.left)

        # if current is parent of largest and largest has no children, 
        # current is second largest
        if current.right and not current.right.left and not current.right.right:
            return current.value

        current = current.right

