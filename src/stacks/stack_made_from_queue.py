from collections import deque
import random
from typing import List


class Stack:
    """A queue implementation of a stack."""

    def __init__(self) -> None:
        """Initialize an instance of Stack."""
        self.queue = deque()

    def __str__(self) -> str:
        """Return a string representation of the stack.

        :return: String representation of the stack.
        """
        if self.is_empty():
            return "The stack is empty!"
        else:
            stack_str = ', '.join(map(str, self.queue))
            return f"Bottom -> {stack_str} <- Top"

    def push(self, num: int) -> None:
        """Push a number onto the stack.

        :param num: The number to push onto the stack.
        """
        self.queue.append(num)

    def pop(self) -> int:
        """Pop the top element from the stack and return it.

        :return: The popped element.
        :raises IndexError: If the stack is empty.
        """
        if self.is_empty():
            raise IndexError("The stack is empty!")

        # Move all elements except the last one to the end of the queue
        for _ in range(len(self.queue) - 1):
            self.push(self.queue.popleft())

        # Pop and return the last element of the queue (or the top element of
        # the stack)
        return self.queue.popleft()

    def peek(self) -> int:
        """Return the top element of the stack without removing it.

        :return: The top element of the stack.
        :raises IndexError: If the stack is empty.
        """
        if self.is_empty():
            raise IndexError("The stack is empty!")

        return self.queue[-1]

    def is_empty(self) -> bool:
        """Check if the stack is empty.

        :return: True if the stack is empty, False otherwise.
        """
        return not self.queue

    def display_stack(self) -> None:
        """Display the stack."""
        print(f"{self}")
        print(f"Is the stack empty? {'Yes' if self.is_empty() else 'No'}")
        if not self.is_empty():
            print(f"The top element of the stack is {self.peek()}.")


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
    stack = Stack()

    print("Before Adding Elements to the Stack")
    stack.display_stack()

    for num in random_nums:
        stack.push(num)
    print("\nAfter Adding Elements to the Stack")
    stack.display_stack()

    popped_element = stack.pop()
    print("\nAfter Popping the Top Element from the Stack")
    stack.display_stack()
    print(f"The element popped from the stack is {popped_element}.")

    while not stack.is_empty():
        stack.pop()
    print("\nAfter Popping the Rest of the Elements from the Stack")
    stack.display_stack()


if __name__ == "__main__":
    main()
