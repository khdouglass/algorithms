def to_kth_node(k, head):
    """Return kth to last node in linked list using length of list."""

    length = 1
    current_node = head

    while current_node.next:
        length += 1 
        current_node = current_node.next

    search_to = length - k

    current_node = head
    for i in range(search_to):
        current_node = current_node.next

    return current_node


def to_kth_node_2(k, head):
    """Return kth to last node in linked list using pointers."""

    left_node = head
    right_node = head

    for i in range(k - 1):
        right_node = right_node.next

    while right_node.next:
        left_node = left_node.next
        right_node = right_node.next

    return left_node