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


def alternate_smallest_integers(integers: List[int]) -> List[int]:
    """Alternately arrange the smallest integers from the input list.

    :param integers: A list of integers.
    :return: A list of integers with the smallest integers arranged alternately.
    """
    heapq.heapify(integers)
    smallest_integers = []

    while integers:
        # Pop the smallest and second-smallest integers from the heap
        smallest = heapq.heappop(integers)
        second_smallest = heapq.heappop(integers)

        # Append the second_smallest and smallest to smallest_integers
        smallest_integers.append(second_smallest)
        smallest_integers.append(smallest)

    return smallest_integers


def main() -> None:
    """Main function."""
    random_ints = generate_random_integers(-100, 100, 6)
    print(f"Smallest Integers: {alternate_smallest_integers(random_ints)}")


if __name__ == "__main__":
    main()
