import random
from typing import List


class MinimumStack:
    """Linked list implementation."""

    def __init__(self) -> None:
        """Initialize an empty linked list."""
        self.stack: List[int] = []
        self.minimum_stack: List[int] = []

    def push(self, num: int) -> None:
        """

        :param num:
        :return:
        """
        self.stack.append(num)

        # Calculate the minimum between num and the current minimum value (if
        # self.minimum_stack is not empty)
        num = min(num, self.min() if self.minimum_stack else num)

        self.minimum_stack.append(num)

    def pop(self) -> int:
        """

        :return:
        """
        self.minimum_stack.pop()
        return self.stack.pop()

    def peek(self) -> int:
        """

        :return:
        :raises IndexError:
        """
        if not self.stack:
            raise IndexError("The stack is empty!")

        return self.stack[-1]

    def min(self) -> int:
        """

        :return:
        :raises IndexError:
        """
        if not self.minimum_stack:
            raise IndexError("The minimum stack is empty!")

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
