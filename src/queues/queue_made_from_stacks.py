import random
from typing import List


class Queue:
    """A queue implemented using two stacks."""

    def __init__(self) -> None:
        """Initialize an empty queue."""
        self.enqueue_stack = []
        self.dequeue_stack = []

    def enqueue(self, num: int) -> None:
        """Add an element to the back of the queue.

        :param num: The element to enqueue.
        """
        self.enqueue_stack.append(num)

    def dequeue(self) -> int:
        """Remove and return the front element of the queue.

        :return: The dequeued element.
        :raises IndexError: If the queue is empty.
        """
        if self.is_empty():
            raise IndexError("The queue is empty!")

        # Transfer all elements from enqueue_stack to dequeue_stack if
        # deque_stack is empty
        self._transfer_elements()

        return self.dequeue_stack.pop()

    def peek(self) -> int:
        """Return the front element of the queue without removing it.

        :return: The front element of the queue.
        :raises IndexError: If the queue is empty.
        """
        if self.is_empty():
            raise IndexError("The queue is empty!")

        # Transfer all elements from enqueue_stack to dequeue_stack if
        # deque_stack is empty
        self._transfer_elements()

        return self.dequeue_stack[-1]

    def _transfer_elements(self) -> None:
        """Transfer elements from enqueue_stack to dequeue_stack."""
        if not self.dequeue_stack:
            while self.enqueue_stack:
                self.dequeue_stack.append(self.enqueue_stack.pop())

    def is_empty(self) -> bool:
        """Check if the queue is empty.

        :return: True if the queue is empty, False otherwise.
        """
        return not (self.enqueue_stack or self.dequeue_stack)

    def display_queue_info(self) -> None:
        """Display information about the queue."""
        print(f"Is the queue empty? {'Yes' if self.is_empty() else 'No'}")
        if not self.is_empty():
            print(f"The front element of the queue is {self.peek()}.")


def generate_random_list(lower: int, upper: int, length: int) -> List[int]:
    """Generate a random list of integers within a specified range.

    :param lower: The lower bound of the range.
    :param upper: The upper bound of the range.
    :param length: The length of the list to generate.
    :return: A list of random integers.
    """
    return [random.randint(lower, upper) for _ in range(length)]


def main() -> None:
    """Main function."""
    random_nums = generate_random_list(1, 10, 10)
    queue = Queue()

    print("Before Enqueueing Elements in the Queue")
    queue.display_queue_info()

    for num in random_nums:
        queue.enqueue(num)
    print("\nAfter Enqueueing Elements in the Queue")
    queue.display_queue_info()

    dequeued_element = queue.dequeue()
    print("\nAfter Dequeueing the Front Element from the Queue")
    queue.display_queue_info()
    print(f"The element dequeued from the queue is {dequeued_element}.")

    while not queue.is_empty():
        queue.dequeue()
    print("\nAfter Dequeueing the Rest of the Elements from the Queue")
    queue.display_queue_info()


if __name__ == "__main__":
    main()
