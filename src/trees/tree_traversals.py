from typing import List


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
        self.nodes_visited = []

    def populate(self) -> None:
        """Populate the binary tree with sample data."""
        self.root = (
            Node(4, Node(2, Node(1), Node(3)), Node(6, Node(5), Node(7)))
        )

    def clear_visited_nodes(self) -> None:
        """Populate the binary tree with sample data."""
        self.nodes_visited.clear()

    def preorder(self, root: Node) -> List[int]:
        """Calculate the height of the binary tree.

        :param root: The root node of the binary tree.
        :return: The height of the binary tree.
        """
        if not root:
            return

        self.nodes_visited.append(root.data)
        self.preorder(root.left)
        self.preorder(root.right)

        return self.nodes_visited

    def inorder(self, root: Node) -> List[int]:
        """Calculate the height of the binary tree.

        :param root: The root node of the binary tree.
        :return: The height of the binary tree.
        """
        if not root:
            return

        self.inorder(root.left)
        self.nodes_visited.append(root.data)
        self.inorder(root.right)

        return self.nodes_visited

    def postorder(self, root: Node) -> List[int]:
        """Calculate the height of the binary tree.

        :param root: The root node of the binary tree.
        :return: The height of the binary tree.
        """
        if not root:
            return

        self.postorder(root.left)
        self.postorder(root.right)
        self.nodes_visited.append(root.data)

        return self.nodes_visited


def main() -> None:
    """Main function."""
    binary_tree = BinaryTree()
    binary_tree.populate()
    root = binary_tree.root

    print(f"Preorder Traversal: {binary_tree.preorder(root)}")
    binary_tree.clear_visited_nodes()

    print(f"Inorder Traversal: {binary_tree.inorder(root)}")
    binary_tree.clear_visited_nodes()

    print(f"Postorder Traversal: {binary_tree.postorder(root)}")


if __name__ == "__main__":
    main()
