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

        for i in range(1, 7):
            string += f"{current.data} -> "
            current = current.next
        string += "3"

        return string

    def populate(self) -> None:
        """Populate the linked list with sample data."""
        self.head = Node(1)
        current, loop_start = self.head, None

        for i in range(2, 7):
            current.next = Node(i)

            if i == 3:
                loop_start = current.next

            current = current.next

        current.next = loop_start

    def create_loop(self, num: int) -> None:
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

    def find_loop_start(self) -> Node:
        """Reverse the linked list in-place."""
        slow, fast = self.head, self.head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                slow = self.head

                while slow != fast:
                    slow = slow.next
                    fast = fast.next

                return slow

        return None


def main() -> None:
    """Main function."""
    linked_list = LinkedList()
    linked_list.populate()

    print("Linked List")
    print(linked_list)

    loop_start_node_num = linked_list.find_loop_start().data
    print(f"\nThe loop starts at Node {loop_start_node_num}!")


if __name__ == "__main__":
    main()
