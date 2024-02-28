import random
from typing import List


class Queue:
    """A stack implementation of a queue."""

    def __init__(self) -> None:
        """Initialize an instance of Queue."""
        self.enqueue_stack = []
        self.dequeue_stack = []

    def __str__(self) -> str:
        """Return a string representation of the queue.

        :return: String representation of the queue.
        """
        if self.is_empty():
            return "The queue is empty!"
        else:
            queue_str = ', '.join(map(str, self.enqueue_stack))
            return f"Front -> {queue_str} <- Back"

    def enqueue(self, num: int) -> None:
        """Enqueue a number into the queue.

        :param num: The number to enqueue into the queue.
        """
        self.enqueue_stack.append(num)

    def dequeue(self) -> int:
        """Dequeue the front element from the queue and return it.

        :return: The dequeued element.
        :raises IndexError: If the queue is empty.
        """
        if self.is_empty():
            raise IndexError("The queue is empty!")

        # Move all elements from enqueue_stack to dequeue_stack
        while self.enqueue_stack:
            self.dequeue_stack.append(self.enqueue_stack.pop())

        # The top element of dequeue_stack represents the front of the queue.
        dequeued_element = self.dequeue_stack.pop()

        # Move the rest of the elements back to the enqueue_stack
        while self.dequeue_stack:
            self.enqueue(self.dequeue_stack.pop())

        return dequeued_element

    def peek(self) -> int:
        """Return the front element of the queue without removing it.

        :return: The front element of the queue.
        :raises IndexError: If the queue is empty.
        """
        if self.is_empty():
            raise IndexError("The queue is empty!")

        # Move all elements from enqueue_stack to dequeue_stack
        while self.enqueue_stack:
            self.dequeue_stack.append(self.enqueue_stack.pop())

        # The top element of dequeue_stack represents the front of the queue.
        front_element = self.dequeue_stack[-1]

        # Move all elements back to the enqueue_stack
        while self.dequeue_stack:
            self.enqueue(self.dequeue_stack.pop())

        return front_element

    def is_empty(self) -> bool:
        """Check if the queue is empty.

        :return: True if the queue is empty, False otherwise.
        """
        return not (self.enqueue_stack or self.dequeue_stack)

    def display_queue(self) -> None:
        """Display the queue."""
        print(f"{self}")
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
    queue.display_queue()

    for num in random_nums:
        queue.enqueue(num)
    print("\nAfter Enqueueing Elements in the Queue")
    queue.display_queue()

    dequeued_element = queue.dequeue()
    print("\nAfter Dequeueing the Front Element from the Queue")
    queue.display_queue()
    print(f"The element dequeued from the queue is {dequeued_element}.")

    while not queue.is_empty():
        queue.dequeue()
    print("\nAfter Dequeueing the Rest of the Elements from the Queue")
    queue.display_queue()


if __name__ == "__main__":
    main()
