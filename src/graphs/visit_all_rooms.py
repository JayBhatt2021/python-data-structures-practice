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
    """Check if it's possible to visit all rooms in a building given keys in
    each room.

    :param rooms: A list of rooms and the keys they hold.
    :return: True if all rooms are visitable, False otherwise.
    """
    # Initialize a set to keep track of visited rooms
    visited_rooms = set()

    def dfs(room: int) -> None:
        """Perform Depth-First Search (DFS) traversal to explore rooms.

        :param room: The current room being visited.
        """
        # Base case: If the room has already been visited, stop exploring.
        if room in visited_rooms:
            return

        # Mark the current room as visited
        visited_rooms.add(room)

        # Explore the rooms accessible from the current room
        for next_room in rooms[room]:
            dfs(next_room)

    # Start DFS traversal from room 0
    dfs(0)

    # Check if all rooms are visited by comparing the count of visited rooms
    # with the total number of rooms
    return len(visited_rooms) == len(rooms)


def main() -> None:
    """Main function."""
    starting_room = 0
    ending_room = 4
    key_count = 3

    # Generate rooms with random keys
    rooms = [
        generate_random_integers(starting_room, ending_room, key_count)
        for _ in range(starting_room, ending_room + 1)
    ]

    # Check if all rooms are visitable
    able_to_visit_str = "Yes" if able_to_visit_all_rooms(rooms) else "No"
    print(
        f"Are you able to visit all the rooms ({rooms}) based on the keys in "
        f"each room? {able_to_visit_str}"
    )


if __name__ == "__main__":
    main()
