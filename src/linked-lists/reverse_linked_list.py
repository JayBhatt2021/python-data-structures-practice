class Node:
    """Node class for a linked list."""

    def __init__(self, data: int) -> None:
        """Initialize a node with data.

        :param data: Data to be stored in the node.
        """
        self.data = data
        self.next = None


class LinkedList:
    """Linked list implementation."""

    def __init__(self) -> None:
        """Initialize an empty linked list."""
        self.head = None

    def __str__(self) -> str:
        """Return a string representation of the linked list.

        :return: String representation of the linked list.
        """
        current, string = self.head, ""

        while current:
            string += f"{current.data} -> "
            current = current.next
        string += "None"

        return string

    def populate(self) -> None:
        """Populate the linked list with sample data."""
        for i in range(1, 6):
            self.append(i)

    def append(self, num: int) -> None:
        """Append a node with given data to the end of the linked list.

        :param num: Data to be appended to the linked list.
        """
        new_node = Node(num)

        if not self.head:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def reverse(self) -> None:
        """Reverse the linked list in-place."""
        previous, current = None, self.head

        while current:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node

        self.head = previous


def main() -> None:
    """Main function."""
    linked_list = LinkedList()
    linked_list.populate()

    print("Original Linked List")
    print(linked_list)

    print("\nReversed Linked List")
    linked_list.reverse()
    print(linked_list)


if __name__ == "__main__":
    main()
