import random
from typing import Dict, List


def generate_random_list(lower: int, upper: int, length: int) -> List[int]:
    """Generate a random list of integers within a specified range.

    :param lower: The lower bound of the range.
    :param upper: The upper bound of the range.
    :param length: The length of the list to generate.
    :return: A list of random integers.
    """
    return [random.randint(lower, upper) for _ in range(length)]


def generate_num_frequency_dict(num_list: List[int]) -> Dict[int, int]:
    """Generate a dictionary containing the frequency of numbers in the list.

    :param num_list: The list of integers.
    :return: A dictionary with integers as keys and their frequencies as values.
    """
    num_freq_dict = {}

    for num in num_list:
        num_freq_dict[num] = num_freq_dict.get(num, 0) + 1

    return num_freq_dict


def print_dictionary(name: str, dictionary: Dict[int, int]) -> None:
    """Print the contents of the dictionary in sorted order.

    :param name: The name of the dictionary.
    :param dictionary: The dictionary to print.
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
