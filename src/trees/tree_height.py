class Node:
    """Node class for a binary tree."""

    def __init__(
            self,
            data: int,
            left: 'Node' = None,
            right: 'Node' = None,
    ) -> None:
        """Initialize a node with data.

        :param data: Data to be stored in the node.
        :param left:
        :param right:
        """
        self.data = data
        self.left = left
        self.right = right


class BinaryTree:
    """Binary tree implementation."""

    def __init__(self) -> None:
        """Initialize a binary tree."""
        self.root = None

    def populate(self) -> None:
        """Populate the binary tree with sample data."""
        self.root = Node(1, Node(2, Node(3, right=Node(4)), Node(5)), Node(6))

    def height(self, node: Node) -> int:
        """Find the start node of the loop in the linked list.

        :return: The start node of the loop if found, None otherwise.
        """
        if not node:
            return 0

        return 1 + max(self.height(node.left), self.height(node.right))


def main() -> None:
    """Main function."""
    binary_tree = BinaryTree()
    binary_tree.populate()
    print(f"Height of the Binary Tree: {binary_tree.height(binary_tree.root)}")


if __name__ == "__main__":
    main()
