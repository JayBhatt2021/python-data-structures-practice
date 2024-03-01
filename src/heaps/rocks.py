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
    """Smash the rocks together to find the weight of the last remaining rock.

    :param rocks: List of weights of the rocks.
    :return: Weight of the last remaining rock after smashing.
    """
    # Convert the rock weights to negative values and create a max heap
    max_heap = [-rock for rock in rocks]
    heapq.heapify(max_heap)

    # Keep smashing rocks until at most one rock remains
    while len(max_heap) > 1:
        # Remove the two heaviest rocks
        heaviest_rock = -heapq.heappop(max_heap)
        second_heaviest_rock = -heapq.heappop(max_heap)

        # If the two heaviest rocks have different weights, smash them together.
        if heaviest_rock != second_heaviest_rock:
            # Add the weight of the smashed rock back to the max heap
            heapq.heappush(max_heap, -(heaviest_rock - second_heaviest_rock))

    # Return the weight of the last remaining rock (or 0 if there are no rocks)
    return -max_heap[0] if max_heap else 0


def main() -> None:
    """Main function."""
    rocks = generate_random_integers(1, 50, 10)
    print(f"Rocks: {rocks}")
    print(f"The weight of the last remaining rock is {smash_rocks(rocks)} kg.")


if __name__ == "__main__":
    main()
