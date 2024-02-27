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

        # Make Node 3 the "last node" for the string representation
        string += f"{current.data}"

        return string

    def populate(self) -> None:
        """Populate the linked list with sample data and create a loop."""
        self.head = Node(1)
        current, loop_start = self.head, None

        for i in range(2, 7):
            current.next = Node(i)
            current = current.next

            if i == 3:
                loop_start = current

        # Create the loop from Node 6 to Node 3
        current.next = loop_start

    def find_loop_start(self) -> Node:
        """Find the start node of the loop in the linked list.

        :return: The start node of the loop if found, None otherwise.
        """
        slow = fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            # Loop is found.
            if slow == fast:
                # Reset the slow pointer back at the head
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

    loop_start_node = linked_list.find_loop_start()
    if loop_start_node:
        print(f"\nThe loop starts at Node {loop_start_node.data}!")
    else:
        print("\nNo loop found in the linked list.")


if __name__ == "__main__":
    main()
