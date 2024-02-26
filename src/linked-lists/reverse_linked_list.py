class Node:
    """"""

    def __init__(self, data: int) -> None:
        """

        :param data:
        """
        self.data = data
        self.next = None


class LinkedList:
    """"""

    def __init__(self) -> None:
        """"""
        self.head = None

    def __str__(self) -> str:
        """

        :return:
        """
        current, string = self.head, ""

        while current:
            string += f"{current.data} -> "
            current = current.next
        string += "None"

        return string

    def populate(self) -> None:
        """

        :return:
        """
        for i in range(1, 6):
            self.append(i)

    def append(self, num: int) -> None:
        """

        :param num:
        :return:
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
        """

        :return:
        """
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
