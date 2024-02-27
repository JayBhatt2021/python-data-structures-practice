import random
from typing import List


class MinimumStack:
    """Stack implementation supporting minimum value retrieval."""

    def __init__(self) -> None:
        """Initialize an instance of MinimumStack."""
        self.stack = []
        self.minimum_stack = []

    def push(self, num: int) -> None:
        """Push a number onto the stack.

        :param num: The number to push onto the stack.
        """
        self.stack.append(num)

        # Calculate the minimum between num and the current minimum number
        # (if self.minimum_stack is not empty)
        minimum = min(num, self.min() if self.minimum_stack else num)

        self.minimum_stack.append(minimum)

    def pop(self) -> int:
        """Pop the top element from the stack and return it.

        :return: The popped element.
        :raises IndexError: If the stack is empty.
        """
        if not self.stack:
            raise IndexError("The stack is empty!")

        self.minimum_stack.pop()
        return self.stack.pop()

    def peek(self) -> int:
        """Return the top element of the stack without removing it.

        :return: The top element of the stack.
        :raises IndexError: If the stack is empty.
        """
        if not self.stack:
            raise IndexError("The stack is empty!")

        return self.stack[-1]

    def min(self) -> int:
        """Return the minimum element in the stack.

        :return: The minimum element in the stack.
        :raises IndexError: If the stack is empty.
        """
        if not self.minimum_stack:
            raise IndexError("The stack is empty!")

        return self.minimum_stack[-1]


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
    total_nums = 14
    random_nums = generate_random_list(-10, 10, total_nums)
    minimum_stack = MinimumStack()

    for num in random_nums:
        minimum_stack.push(num)

    print("Before Popping Half of the Stack")
    print(f"Top Value of the Stack: {minimum_stack.peek()}")
    print(f"Minimum Value of the Stack: {minimum_stack.min()}")

    for _ in range(total_nums // 2):
        minimum_stack.pop()

    print("\nAfter Popping Half of the Stack")
    print(f"Top Value of the Stack: {minimum_stack.peek()}")
    print(f"Minimum Value of the Stack: {minimum_stack.min()}")


if __name__ == "__main__":
    main()
