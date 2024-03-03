from typing import List


class Node:
    """Node class for a graph."""

    def __init__(self, value: int, neighbors: List["Node"] = None) -> None:
        """Initialize a node with a value and its neighbors.

        :param value: The value of the node.
        :param neighbors: The list of neighboring nodes.
        """
        self.value = value
        self.neighbors = neighbors or []

    def __str__(self) -> str:
        """Return a string representation of the node.

        :return: A string representation of the node.
        """
        return str(self.value)


class Graph:
    """Graph implementation."""

    def __init__(self, nodes: List[Node] = None) -> None:
        """Initialize a graph with nodes.

        :param nodes: The list of nodes in the graph.
        """
        self.nodes = nodes or []

    def __str__(self) -> str:
        """Return a string representation of the graph.

        :return: A string representation of the graph.
        """
        return f"[{', '.join(map(str, self.nodes))}]"

    def __eq__(self, other: object) -> bool:
        """Check if two graphs are equal.

        :param other: Another object to compare with.
        :return: True if two graphs are equal, False otherwise.
        """
        # Return False if the other object is not a graph
        if not isinstance(other, Graph):
            return False

        # Sort the nodes of both graphs for consistent comparison
        sorted_self_nodes = sorted(self.nodes, key=lambda x: x.value)
        sorted_other_nodes = sorted(other.nodes, key=lambda x: x.value)

        # Check if the values of corresponding nodes are equal
        for self_node, other_node in zip(sorted_self_nodes, sorted_other_nodes):
            if self_node.value != other_node.value:
                return False

        return True

    def populate(self) -> None:
        """Populate the graph with sample data."""
        # Create nodes for each value in [1, 2, 3, 4]
        nodes_dict = {num: Node(num) for num in range(1, 5)}

        # Populate the neighbors for each node
        nodes_dict[1].neighbors.extend([nodes_dict[2], nodes_dict[4]])
        nodes_dict[2].neighbors.extend([nodes_dict[1], nodes_dict[3]])
        nodes_dict[3].neighbors.extend([nodes_dict[2], nodes_dict[4]])
        nodes_dict[4].neighbors.extend([nodes_dict[1], nodes_dict[3]])

        # Populate the graph with nodes
        self.nodes.extend(nodes_dict.values())

    def clone_graph(self) -> "Graph":
        """Create a deep-copy of this graph.

        :return: A new graph object representing the cloned graph.
        """
        # Return an empty graph if this graph has no nodes
        if not self.nodes:
            return Graph()

        # Get the starting node of the original graph
        start_node = self.nodes[0]

        # Initialize a dictionary to map the original nodes to their
        # corresponding clones
        original_to_clone = {}

        def dfs(node: Node) -> Node:
            """Perform Depth-First Search traversal to clone the graph.

            :param node: The current node being visited.
            :return: The cloned node.
            """
            # Base case: If the current node has been visited before, return its
            # corresponding clone.
            if node in original_to_clone:
                return original_to_clone[node]

            # Create a clone of the current node
            clone = Node(node.value)

            # Add the original node and its clone to the mapping dictionary
            original_to_clone[node] = clone

            # Clone the neighbors of the current node recursively
            clone.neighbors = [dfs(neighbor) for neighbor in node.neighbors]

            # Return the clone of the current node
            return clone

        # Clone the graph starting from the specified node
        dfs(start_node)

        # Return a new graph containing the cloned nodes
        return Graph(list(original_to_clone.values()))


def main() -> None:
    """Main function."""
    graph = Graph()
    graph.populate()
    cloned_graph = graph.clone_graph()

    graph_equality_str = "Yes" if graph == cloned_graph else "No"
    print(
        f"Does the original graph ({graph}) contain the same values as the "
        f"cloned graph ({cloned_graph})? {graph_equality_str}"
    )


if __name__ == "__main__":
    main()
