import heapq
import random
from typing import List


class LargestListElements:
    """A class designed to efficiently manage and retrieve the largest elements
    up to a specified position within a list.
    """

    def __init__(self, elements: List[int], position: int) -> None:
        """Initialize an instance of LargestListElements.

        :param elements: The list of elements.
        :param position: The position to track the largest elements.
        :raise ValueError: If the position is invalid.
        """
        # Obtaining the "0th" (or lower) largest element doesn't make logical
        # sense. Additionally, the position has to be at most len(elements) + 1
        # to prevent an IndexError from occurring in the append method.
        if position < 1 or position > len(elements) + 1:
            raise ValueError("Invalid value for the position!")

        self.min_heap = elements
        self.position = position

        # Sort the elements from smallest to largest
        heapq.heapify(self.min_heap)

        # Remove any elements that are smaller than the "position"th largest
        # element
        while len(self.min_heap) > position:
            heapq.heappop(self.min_heap)

    def __str__(self) -> str:
        """Return the string representation of LargestListElements.

        :return: The string representation of LargestListElements.
        """
        return str(self.min_heap)

    def append(self, element: int) -> int:
        """Append an element to the min heap and maintain the "position" largest
        elements.

        :param element: The element to append.
        :return: The "position"th largest element after appending.
        """
        heapq.heappush(self.min_heap, element)

        # Maintain the "position" largest elements in the min heap
        if len(self.min_heap) > self.position:
            heapq.heappop(self.min_heap)

        return self.min_heap[0]


def generate_random_integers(lower: int, upper: int, length: int) -> List[int]:
    """Generate a list of random integers within a specified range.

    :param lower: The lower bound of the range.
    :param upper: The upper bound of the range.
    :param length: The length of the list to generate.
    :return: A list of random integers.
    """
    return [random.randint(lower, upper) for _ in range(length)]


def main() -> None:
    """Main function."""
    random_ints = generate_random_integers(-50, 50, 6)
    position = 4
    largest_list_elements = LargestListElements(random_ints, position)

    append_elements = generate_random_integers(-40, 20, 3)
    for i, num in enumerate(append_elements):
        print(f"Appending {num} to {largest_list_elements}...")
        position_largest_element = largest_list_elements.append(num)

        print(
            f"The {position}th largest element in {largest_list_elements} is "
            f"{position_largest_element}."
        )

        if i != len(append_elements) - 1:
            print()


if __name__ == "__main__":
    main()
