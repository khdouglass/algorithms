class GraphNode:
    """Create graph nodes."""

    def __init__(self, label):
        self.label = label
        self.neighbors = set()
        self.color = None


def color_graph(graph, colors):
    """Assign colors to nodes in a graph. Legal coloring
    means we have no adjacent colors.
    """

    for node in graph:
        if node in node.neighbors:
            raise Exception('Legal coloring impossible for node with loop: %s' % node.label)

        # get node's neighbors' colors so we can check if a color is illegal in constant time
        illegal_colors = set([neighbor.color for neighbor in node.neighbors if neighbor.color])

        # assign the first legal color
        for color in colors:
            if color not in illegal_colors:
                node.color = color
                break
