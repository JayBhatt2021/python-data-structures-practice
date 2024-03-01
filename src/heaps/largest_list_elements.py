import heapq
import random
from typing import List


class LargestListElements:
    """Replace this"""

    def __init__(self, elements: List[int], position: int) -> None:
        """

        :param elements:
        :param position:
        :return:
        :raise Exception:
        """
        if not elements:
            raise Exception("The element list must be populated with elements!")

        if position < 1:
            raise Exception(
                'Returning "0th" (or lower) largest element does not make '
                'logical sense.'
            )

        if position > len(elements):
            raise Exception(
                "The position cannot exceed the length of the element list!"
            )

        self.min_heap = elements
        self.position = position

        heapq.heapify(self.min_heap)

        while len(self.min_heap) > position:
            heapq.heappop(self.min_heap)

    def __str__(self) -> str:
        """

        :return:
        """
        return str(self.min_heap)

    def append(self, element: int) -> int:
        """

        :param element:
        :return:
        """
        heapq.heappush(self.min_heap, element)

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
        position_element = largest_list_elements.append(num)
        print(
            f"The {position}th largest element in {largest_list_elements} is "
            f"{position_element}."
        )
        if i != len(append_elements) - 1:
            print()


if __name__ == "__main__":
    main()
