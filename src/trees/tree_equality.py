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

    def __eq__(self, other: object) -> bool:
        """Check if two binary trees are equal.

        :param other: Another object to compare.
        :return: True if the trees are equal, False otherwise.
        """
        return isinstance(other, BinaryTree) and self._are_trees_equal(
            self.root, other.root
        )

    def populate(self) -> None:
        """Populate the binary tree with sample data."""
        self.root = Node(9, right=Node(5, Node(3, Node(11), Node(7))))

    def _are_trees_equal(self, self_root: Node, other_root: Node) -> bool:
        """Check if two trees are equal recursively.

        :param self_root: Root of the first tree.
        :param other_root: Root of the second tree.
        :return: True if the trees are equal, False otherwise.
        """
        # Base case #1: Both nodes are "None".
        if not self_root and not other_root:
            return True

        # Base case #2: One node is "None" while the other node is not "None".
        if not self_root or not other_root:
            return False

        # Recursive step: The two trees are equal if their roots, left subtrees,
        # and right subtrees are equal.
        return (
            self_root.data == other_root.data
            and self._are_trees_equal(self_root.left, other_root.left)
            and self._are_trees_equal(self_root.right, other_root.right)
        )


def main() -> None:
    """Main function."""
    binary_tree_one = binary_tree_two = BinaryTree()

    equality_str = "Yes" if binary_tree_one == binary_tree_two else "No"
    print(f"Is binary_tree_one equal to binary_tree_two?: {equality_str}")


if __name__ == "__main__":
    main()
