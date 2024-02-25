from typing import List
import random


def generate_random_list(lower: int, upper: int, length: int) -> List[int]:
    """Generates a random list of integers within a specified range.

    :param lower: The lower bound of the range.
    :param upper: The upper bound of the range.
    :param length: The length of the list to generate.
    :return: A list of random integers.
    """
    return [random.randint(lower, upper) for _ in range(length)]


def binary_search(num_list: List[int], key: int) -> int:
    """Performs binary search to find the index of a key in a sorted list.

    :param num_list: The list of integers to search.
    :param key: The key to search for.
    :return: The index of the key if found, otherwise -1.
    """
    left, right = 0, len(num_list) - 1

    while left <= right:
        middle = (left + right) // 2

        if num_list[middle] == key:
            return middle
        elif num_list[middle] < key:
            left = middle + 1
        else:
            right = middle - 1

    return -1


def main() -> None:
    """Main function."""
    num_list, key = sorted(generate_random_list(-10, 10, 20)), 3
    key_index = binary_search(num_list, key)

    if key_index == -1:
        print(f"{key} was not found!")
    else:
        print(f"{key} was found at index {key_index}!")


if __name__ == "__main__":
    main()
