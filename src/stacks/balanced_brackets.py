def is_balanced(bracket_string: str) -> bool:
    """Generate a random list of integers within a specified range.

    :param string:
    :return: A list of random integers.
    """
    if len(bracket_string) % 2 == 1:
        return False

    bracket_dict = {")": "(", "]": "[", "}": "{"}
    stack = []

    for bracket in bracket_string:
        if bracket in bracket_dict:
            if stack and bracket_dict[bracket] == stack[-1]:
                stack.pop()
            else:
                return False
        else:
            stack.append(bracket)

    return not len(stack)


def main() -> None:
    """Main function."""
    bracket_strings = ["[]", "()}", "{", "{)", "", "({[]})", "{}()[]", "][}{()"]

    for bracket_str in bracket_strings:
        is_balanced_str = "Yes" if is_balanced(bracket_str) else "No"
        print(f'Is "{bracket_str}" balanced? {is_balanced_str}')


if __name__ == "__main__":
    main()
