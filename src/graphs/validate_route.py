from typing import List


class Node:
    """Node class for a graph."""

    def __init__(self, name: str, neighbors: List["Node"] = None) -> None:
        """Initialize a node with a name and its neighbors.

        :param name: The name of the node.
        :param neighbors: The list of neighboring nodes.
        """
        self.name = name
        self.neighbors = neighbors or []


class Graph:
    """Graph implementation."""

    def __init__(self, nodes: List[Node] = None) -> None:
        """Initialize a graph with nodes.

        :param nodes: The list of nodes in the graph.
        """
        self.nodes = nodes or []

    def populate(self) -> None:
        """Populate the graph with sample data."""
        # Create nodes for each letter in "ABCDEFG"
        nodes_dict = {name: Node(name) for name in "ABCDEFG"}

        # Populate the neighbors for each node
        nodes_dict["A"].neighbors.extend([nodes_dict["B"], nodes_dict["C"]])
        nodes_dict["B"].neighbors.extend([nodes_dict["C"], nodes_dict["D"]])
        nodes_dict["C"].neighbors.extend([nodes_dict["F"]])
        nodes_dict["D"].neighbors.extend([nodes_dict["E"], nodes_dict["G"]])
        nodes_dict["E"].neighbors.extend([nodes_dict["C"], nodes_dict["G"]])
        nodes_dict["F"].neighbors.extend([nodes_dict["G"]])

        # Populate the graph with nodes
        self.nodes.extend(nodes_dict.values())

    def is_connected(self, start: str, end: str) -> bool:
        """Check if there's a path between two nodes using Depth-First Search.

        :param start: The name of the starting node.
        :param end: The name of the ending node.
        :return: True if there's a path between start and end, False otherwise.
        """
        # Initialize the starting and ending nodes
        start_node = self._find_node_by_name(start)
        end_node = self._find_node_by_name(end)

        # There is no connection between the starting and ending nodes if either
        # of them doesn't exist.
        if not start_node or not end_node:
            return False

        # Initialize the set of visited nodes
        visited = set()

        def dfs(node: Node) -> bool:
            """Perform Depth-First Search traversal to find a path between two
            nodes.

            :param node: The current node being visited.
            :return: True if a path is found to the end node, False otherwise.
            """
            # Base case #1: If the node has already been visited, return False
            # to prevent revisiting it.
            if node in visited:
                return False

            # Base case #2: If the current node is the target node, return True
            # indicating that a path is found.
            if node == end_node:
                return True

            # Mark the current node as visited
            visited.add(node)

            # Recursively explore each neighbor of the current node (If any
            # neighbor returns True (indicating a path is found), return True).
            return any(dfs(neighbor) for neighbor in node.neighbors)

        # Use the inner method to determine the connection
        return dfs(start_node)

    def _find_node_by_name(self, name: str) -> Node:
        """Find a node in the graph by its name.

        :param name: The name of the node to find.
        :return: The node if found, otherwise None.
        """
        for node in self.nodes:
            if node.name == name:
                return node


def main() -> None:
    """Main function."""
    start = "A"
    end = "G"
    graph = Graph()

    graph.populate()
    is_connected_str = "Yes" if graph.is_connected(start, end) else "No"
    print(f"Is Node {start} connected to Node {end}? {is_connected_str}")


if __name__ == "__main__":
    main()
