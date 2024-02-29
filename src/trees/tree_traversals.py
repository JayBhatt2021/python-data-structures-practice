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

    def populate(self) -> None:
        """Populate the binary tree with sample data."""
        self.root = (
            Node(4, Node(2, Node(1), Node(3)), Node(6, Node(5), Node(7)))
        )

    def obtain_preorder_nodes(self) -> List[int]:
        """Calculate the height of the binary tree.

        :return: The height of the binary tree.
        """
        nodes_visited = []

        def preorder(root: Node) -> None:
            """

            :param root:
            """
            if not root:
                return

            nodes_visited.append(root.data)
            preorder(root.left)
            preorder(root.right)

        preorder(self.root)

        return nodes_visited

    def obtain_inorder_nodes(self) -> List[int]:
        """Calculate the height of the binary tree.

        :return: The height of the binary tree.
        """
        nodes_visited = []

        def inorder(root: Node) -> None:
            """

            :param root:
            """
            if not root:
                return

            inorder(root.left)
            nodes_visited.append(root.data)
            inorder(root.right)

        inorder(self.root)

        return nodes_visited

    def obtain_postorder_nodes(self) -> List[int]:
        """Calculate the height of the binary tree.

        :return: The height of the binary tree.
        """
        nodes_visited = []

        def postorder(root: Node) -> None:
            """

            :param root:
            """
            if not root:
                return

            postorder(root.left)
            postorder(root.right)
            nodes_visited.append(root.data)

        postorder(self.root)

        return nodes_visited


def main() -> None:
    """Main function."""
    binary_tree = BinaryTree()
    binary_tree.populate()

    print(f"Preorder Traversal: {binary_tree.obtain_preorder_nodes()}")
    print(f"Inorder Traversal: {binary_tree.obtain_inorder_nodes()}")
    print(f"Postorder Traversal: {binary_tree.obtain_postorder_nodes()}")


if __name__ == "__main__":
    main()
