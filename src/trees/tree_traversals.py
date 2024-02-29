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

    def preorder_traversal(self) -> List[int]:
        """Perform a preorder traversal of the binary tree.

        :return: List of nodes visited in preorder.
        """
        nodes_visited = []

        def traverse(root: Node) -> None:
            """Recursive helper function for preorder traversal.

            :param root: The root node of the subtree.
            """
            # Base case: If the current node is "None", stop traversing further.
            if not root:
                return

            # Recursive step (preorder): Center, Left, Right
            nodes_visited.append(root.data)
            traverse(root.left)
            traverse(root.right)

        traverse(self.root)

        return nodes_visited

    def inorder_traversal(self) -> List[int]:
        """Perform an inorder traversal of the binary tree.

        :return: List of nodes visited in inorder.
        """
        nodes_visited = []

        def traverse(root: Node) -> None:
            """Recursive helper function for inorder traversal.

            :param root: The root node of the subtree.
            """
            # Base case: If the current node is "None", stop traversing further.
            if not root:
                return

            # Recursive step (inorder): Left, Center, Right
            traverse(root.left)
            nodes_visited.append(root.data)
            traverse(root.right)

        traverse(self.root)

        return nodes_visited

    def postorder_traversal(self) -> List[int]:
        """Perform a postorder traversal of the binary tree.

        :return: List of nodes visited in postorder.
        """
        nodes_visited = []

        def traverse(root: Node) -> None:
            """Recursive helper function for postorder traversal.

            :param root: The root node of the subtree.
            """
            # Base case: If the current node is "None", stop traversing further.
            if not root:
                return

            # Recursive step (postorder): Left, Right, Center
            traverse(root.left)
            traverse(root.right)
            nodes_visited.append(root.data)

        traverse(self.root)

        return nodes_visited


def main() -> None:
    """Main function."""
    binary_tree = BinaryTree()
    binary_tree.populate()

    print(f"Preorder Traversal: {binary_tree.preorder_traversal()}")
    print(f"Inorder Traversal: {binary_tree.inorder_traversal()}")
    print(f"Postorder Traversal: {binary_tree.postorder_traversal()}")


if __name__ == "__main__":
    main()
