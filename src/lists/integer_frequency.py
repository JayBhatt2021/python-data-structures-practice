from typing import Dict, List
import random


def generate_random_list(lower: int, upper: int, length: int) -> List[int]:
    """Generates a random list of integers within a specified range.

    :param lower: The lower bound of the range.
    :param upper: The upper bound of the range.
    :param length: The length of the list to generate.
    :return: A list of random integers.
    """
    return [random.randint(lower, upper) for _ in range(length)]


def generate_num_frequency_dict(num_list: List[int]) -> Dict[int, int]:
    """Performs binary search to find the index of a key in a sorted list.

    :param num_list: The list of integers to search.
    :param key: The key to search for.
    :return: The index of the key if found, otherwise -1.
    """
    num_freq_dict = {}

    for num in num_list:
        num_freq_dict[num] = num_freq_dict.get(num, 0) + 1

    return num_freq_dict


def print_dictionary(name: str, dictionary: Dict[int, int]) -> None:
    """Performs binary search to find the index of a key in a sorted list.

    :param num_list: The list of integers to search.
    :param key: The key to search for.
    :return: The index of the key if found, otherwise -1.
    """
    print(name)
    for key, value in sorted(dictionary.items()):
        print(f"{key} -> {value}")


def main() -> None:
    """Main function."""
    num_list = generate_random_list(1, 5, 100)
    num_freq_dict = generate_num_frequency_dict(num_list)
    print_dictionary("Frequency of Numbers", num_freq_dict)


if __name__ == "__main__":
    main()
