from typing import List
import random


def generate_random_list(lower, upper, length) -> List[int]:
    """

    :param lower:
    :param upper:
    :param length:
    :return:
    """
    return [random.randint(lower, upper) for _ in range(length)]


def binary_search(num_list: List[int], key: int) -> int:
    """

    :param num_list:
    :return:
    """
    left, right = 0, len(num_list) - 1

    while left < right:
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
