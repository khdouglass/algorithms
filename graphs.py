def are_connected(self, thing1, thing2):
    """Breadth-first search to see if two 'things' are connected."""

    # create queue to store possible nodes to check
    possible_nodes = Queue()
    # create set to track which nodes haven been checked/seen
    seen = set()
    # add starting point 'thing' to queue and seen
    possible_nodes.enqueue(thing1)
    seen.add(thing1)

    # while there are still things to check
    while not possible_nodes.is_empty():
        # look at first item in queue
        thing = possible_nodes.dequeue()
        # return True if it's what we're looking for
        if thing is thing2:
            return True
        # otherwise, add things from thing's adjacency list to check 
        else:
            for thing in thing.adjacent - seen:
                possible_nodes.enqueue(thing)
                seen.add(thing)
    return False


def are_connected_recursive(self, thing1, thing2, seen=None):
    """Recursive depth-first search to see if two 'things' are connected."""

    # if set is not passed through (first call), create set
    if not seen:
        seen = set()

    # return True if thing matches what we're looking for
    if thing1 is thing2:
        return True

    # if not, add thing to seen list
    seen.add(thing1)

    # add thing's adjacency list to seen and recursively call function on them
    for thing in thing1.adjacent - seen:
        if self.are_connected_recursive(person, person2, seen):
            return True
    return False
    