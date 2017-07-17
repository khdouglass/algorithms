class Node(object):
    def __init__(self, data):
        """Contructor to initialize node object."""
        self.data = data
        self.next = None

class LinkedList(object):
    def __init__(self):
        """Initialize head of Linked List."""
        self.head = None

    def push(self, new_data):
        """Add new node to beginning of list."""
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def add_two_lists(self, first, second):
        prev = None
        temp = None
        carry = 0

        # while both lists exist
        while(first is not None or second is not None):
            first_data = 0 if first is None else first.data
            second_data = 0 if second is None else second.data
            # total is sum of carry, next digit of 1st list, next digit of 2nd list
            total = carry + first_data + second_data

            # update carry for next calculation
            carry = 1 if total >= 10 else 0

            # updat total if it is greater than 10
            total = total if total < 10 else total % 10

            # create new node with total as data
            temp = Node(total)

            # it this is firts node, set it as head
            if self.head is None:
                self.head = temp
            else:
                prev.next = temp

            # set prev for next insertion
            prev = temp

            # move first and second pointers to next nodes
            if first is not None:
                first = first.next
            if second is not None:
                second = second.next

        if carry > 0: 
            temp.next = Node(carry)

    def print_list(self):
        """Print linked list."""
        temp = self.head
        while temp:
            print temp.data
            temp = temp.next


