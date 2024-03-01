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


def smash_rocks(rocks: List[int]) -> int:
    """Generate a list of random integers within a specified range.

    :param lower: The lower bound of the range.
    :return: A list of random integers.
    """
    max_heap = [-r for r in rocks]
    heapq.heapify(max_heap)

    while len(max_heap) > 1:
        heaviest_rock = -heapq.heappop(max_heap)
        second_heaviest_rock = -heapq.heappop(max_heap)

        if heaviest_rock != second_heaviest_rock:
            heapq.heappush(max_heap, -(heaviest_rock - second_heaviest_rock))

    return -max_heap[0] if max_heap else 0


def main() -> None:
    """Main function."""
    rocks = generate_random_integers(1, 50, 10)
    print(f"Rocks: {rocks}")
    print(f"The weight of the last rock is {smash_rocks(rocks)} kilograms.")


if __name__ == "__main__":
    main()
