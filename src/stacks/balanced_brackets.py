def is_balanced(bracket_string: str) -> bool:
    """Check if the bracket string is balanced.

    :param bracket_string: The string containing brackets.
    :return: True if the brackets are balanced, False otherwise.
    """
    # Bracket strings of odd lengths will always be unbalanced.
    if len(bracket_string) % 2 == 1:
        return False

    bracket_dict = {")": "(", "]": "[", "}": "{"}
    stack = []

    for bracket in bracket_string:
        if bracket in bracket_dict:
            if stack and bracket_dict[bracket] == stack[-1]:
                # Remove the opening bracket from the stack if it matches the
                # incoming closing bracket
                stack.pop()
            else:
                # Return False if the stack is empty OR the opening bracket from
                # the stack does NOT match the incoming closing bracket
                return False
        else:
            # Push the opening bracket on the stack
            stack.append(bracket)

    # Returns True if all opening brackets are removed
    return not stack


def main() -> None:
    """Main function."""
    bracket_strings = ["[]", "()}", "{", "{)", "", "({[]})", "{}()[]", "][}{)("]

    for bracket_str in bracket_strings:
        is_balanced_str = "Yes" if is_balanced(bracket_str) else "No"
        print(f'Is "{bracket_str}" balanced? {is_balanced_str}')


if __name__ == "__main__":
    main()
