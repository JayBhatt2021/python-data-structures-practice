import heapq
import random
from typing import List


def generate_random_integers(lower: int, upper: int, length: int) -> List[int]:
    """Generate a list of random integers within a specified range.

    :param lower: The lower bound of the range.
    :param upper: The upper bound of the range.
    :param length: The length of the list to generate.
    :return: A list of random integers.
    """
    return [random.randint(lower, upper) for _ in range(length)]


def remove_smallest_integers(integers: List[int]) -> List[int]:
    """

    :param integers:
    :return:
    """
    heapq.heapify(integers)
    smallest_integers = []

    while integers:
        smallest = heapq.heappop(integers)
        second_smallest = heapq.heappop(integers)
        smallest_integers.append(second_smallest)
        smallest_integers.append(smallest)

    return smallest_integers


def main() -> None:
    """Main function."""
    random_ints = generate_random_integers(-100, 100, 20)
    print(f"Smallest Integers: {remove_smallest_integers(random_ints)}")


if __name__ == "__main__":
    main()
