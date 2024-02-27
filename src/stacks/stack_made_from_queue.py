from collections import deque
import random
from typing import List


class Stack:
    """Stack implementation supporting minimum value retrieval."""

    def __init__(self) -> None:
        """Initialize an instance of MinimumStack."""
        self.queue = deque()

    def __str__(self) -> str:
        """

        :return:
        """
        if self.is_empty():
            return "The stack is empty!"
        else:
            stack_str = ', '.join([str(num) for num in self.queue])
            return f"Bottom -> {stack_str} <- Top"

    def pop(self) -> int:
        """Pop the top element from the stack and return it.

        :return: The popped element.
        :raises IndexError: If the stack is empty.
        """
        if self.is_empty():
            raise IndexError("The stack is empty!")

        for i in range(len(self.queue) - 1):
            self.push(self.queue.popleft())

        return self.queue.popleft()

    def push(self, num: int) -> None:
        """Push a number onto the stack.

        :param num: The number to push onto the stack.
        """
        self.queue.append(num)

    def peek(self) -> int:
        """Return the top element of the stack without removing it.

        :return: The top element of the stack.
        :raises IndexError: If the stack is empty.
        """
        if self.is_empty():
            raise IndexError("The stack is empty!")

        return self.queue[-1]

    def display_stack(self) -> None:
        """Generate a random list of integers within a specified range.

        :param lower: The lower bound of the range.
        :param upper: The upper bound of the range.
        :param length: The length of the list to generate.
        :return: A list of random integers.
        """
        print(f"{self}")
        print(f"Is the stack empty? {'Yes' if self.is_empty() else 'No'}")

    def is_empty(self) -> bool:
        """Return the minimum element in the stack.

        :return: The minimum element in the stack.
        :raises IndexError: If the stack is empty.
        """
        return not self.queue


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
    total_nums = 10
    random_nums = generate_random_list(1, 10, total_nums)
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
