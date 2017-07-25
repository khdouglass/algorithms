"""Is this binary search tree a valid BST?

A valid binary search tree follows a specific rule. In our case,
the rule is "left child must value must be less-than parent-value"
and "right child must be greater-than-parent value".

This rule is recursive, so *everything* left of a parent
must less than that parent (even grandchildren or deeper)
and everything right of a parent must be greater than.

For example, this tree is valid::

        4
     2     6
    1 3   5 7

Let's create this tree and test that::

    >>> t = Node(4,
    ...       Node(2, Node(1), Node(3)),
    ...       Node(6, Node(5), Node(7))
    ... )

    >>> t.is_valid()
    True

This tree isn't valid, as the left-hand 3 is wrong (it's less
than 2)::

        4
     2     6
    3 3   5 7

Let's make sure that gets caught::

    >>> t = Node(4,
    ...       Node(2, Node(3), Node(3)),
    ...       Node(6, Node(5), Node(7))
    ... )

    >>> t.is_valid()
    False

This tree is invalid, as the bottom-right 1 is wrong --- it is
less than its parent, 6, but it's also less than its grandparent,
4, and therefore should be left of 4::

        4
     2     6
    1 3   1 7

    >>> t = Node(4,
    ...       Node(2, Node(1), Node(3)),
    ...       Node(6, Node(1), Node(7))
    ... )

    >>> t.is_valid()
    False
"""


class Node:
    """Binary search tree node."""

    def __init__(self, data, left=None, right=None):
        """Create node, with data and optional left/right."""

        self.left = left
        self.right = right
        self.data = data

    def is_valid(self):
        """Is this tree a valid BST?"""

        def _ok(n, lt, gt):
            """Check this node & recurse to children
               lt: left children must be <= this
               gt: right children must be >= this
            """

            if n is None: 
                # base case -- this is not a node
                return True

            if lt is not None and n.data > lt:
                # base case -- left is bigger than allowed, fail fast
                return False

            if gt is not None and n.data < gt:
                # base case -- right is smaller than allowed, fail fast
                return False

            if not _ok(n.left, n.data, gt):
                # general case -- check our left child, all descendants must be 
                # less than our data, if not, fail fast
                return False

            if not _ok(n.right, lt, n.data):
                # general case -- check our right child, all descendants must eb
                # greater than our data, if not, fail fast
                return False

            # if reach here, we're either a leaf node with valid data for lt/gt
            # or higher up -- either way, this is winning base case
            return True

        # call recursive function -- pass None as lt and gt since we haven't gone
        # left or right and don't know those values yet
        return _ok(self, None, None)




if __name__ == "__main__":
    import doctest

    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED; THAT'S VALID!\n"
