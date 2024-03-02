from typing import List


class Node:
    """Node class for a graph."""

    def __init__(self, name: str) -> None:
        """Initialize a node with a name.

        :param name: The name of the node.
        """
        self.name = name
        self.neighbors: List["Node"] = []


class Graph:
    """Graph implementation."""

    def __init__(self) -> None:
        """Initialize a graph."""
        self.nodes: List[Node] = []

    def populate(self) -> None:
        """Populate the graph with sample data."""
        nodes_dict = {name: Node(name) for name in "ABCDEFG"}

        nodes_dict["A"].neighbors.extend([nodes_dict["B"], nodes_dict["C"]])
        nodes_dict["B"].neighbors.extend([nodes_dict["C"], nodes_dict["D"]])
        nodes_dict["C"].neighbors.extend([nodes_dict["F"]])
        nodes_dict["D"].neighbors.extend([nodes_dict["E"], nodes_dict["G"]])
        nodes_dict["E"].neighbors.extend([nodes_dict["C"], nodes_dict["G"]])
        nodes_dict["F"].neighbors.extend([nodes_dict["G"]])

        self.nodes.extend(nodes_dict.values())

    def is_connected(self, start: str, end: str) -> bool:
        """Check if there's a path between two nodes using Depth-First Search.

        :param start: The name of the starting node.
        :param end: The name of the ending node.
        :return: True if there's a path between start and end, False otherwise.
        """
        start_node = self._find_node_by_name(start)
        end_node = self._find_node_by_name(end)

        if not start_node or not end_node:
            return False

        visited_set = set()

        def dfs(node: Node) -> bool:
            """Perform Depth-First Search traversal to find a path between two
            nodes.

            :param node: The current node being visited.
            :return: True if a path is found to the end node, False otherwise.
            """
            if node in visited_set:
                return False

            if node == end_node:
                return True

            visited_set.add(node)

            # Recursively traverse through neighbors to find a path
            return any(dfs(neighbor) for neighbor in node.neighbors)

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
    end = "E"
    graph = Graph()

    graph.populate()
    is_connected_str = "Yes" if graph.is_connected(start, end) else "No"
    print(f"Is Node {start} connected to Node {end}? {is_connected_str}")


if __name__ == "__main__":
    main()
