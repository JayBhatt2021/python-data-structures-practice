class Node:
    """Node class for a binary tree."""

    def __init__(
        self,
        data: int,
        left: "Node" = None,
        right: "Node" = None,
    ) -> None:
        """Initialize a node with data.

        :param data: Data to be stored in the node.
        :param left: Left child node.
        :param right: Right child node.
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
        """Calculate the height of the binary tree.

        :param node: The root node of the binary tree.
        :return: The height of the binary tree.
        """
        # Base case: The height of a "None" node is 0.
        if not node:
            return 0

        left_height = self.height(node.left)
        right_height = self.height(node.right)

        # Recursive step: The height of the tree is 1 (the height of the current
        # node) plus the height of the tallest child.
        return 1 + max(left_height, right_height)


def main() -> None:
    """Main function."""
    binary_tree = BinaryTree()
    binary_tree.populate()

    height = binary_tree.height(binary_tree.root)
    print(f"Height of the Binary Tree: {height} node(s)")


if __name__ == "__main__":
    main()
