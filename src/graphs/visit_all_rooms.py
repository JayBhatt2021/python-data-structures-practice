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


def able_to_visit_all_rooms(rooms: List[List[int]]) -> bool:
    """

    :param rooms:
    :return:
    """
    visited_rooms = set()

    def dfs(room):
        """

        :param room:
        :return:
        """
        if room in visited_rooms:
            return

        visited_rooms.add(room)

        for room in rooms[room]:
            dfs(room)

    dfs(0)

    return len(visited_rooms) == len(rooms)


def main() -> None:
    """Main function."""
    starting_room = 0
    ending_room = 4
    key_count = 3
    rooms = [
        generate_random_integers(starting_room, ending_room, key_count)
        for _ in range(starting_room, ending_room + 1)
    ]

    able_to_visit_str = "Yes" if able_to_visit_all_rooms(rooms) else "No"
    print(
        f"Are you able to visit all the rooms ({rooms}) based on the keys in "
        f"each room? {able_to_visit_str}"
    )


if __name__ == "__main__":
    main()
