from typing import List


def print_matrix(matrix: List[List[int]]) -> None:
    """Print the matrix.

    :param matrix: The matrix to print.
    """
    for row in matrix:
        print(*row)


def rotate_90_degrees(matrix: List[List[int]]) -> None:
    """Rotate the matrix 90 degrees clockwise in-place.

    :param matrix: The matrix to rotate.
    :raises ValueError: If the matrix is not square.
    """
    n = len(matrix)
    if any(len(row) != n for row in matrix):
        raise ValueError("The matrix must be square.")

    left, right = 0, n - 1

    while left < right:

        # Offset represents distance from corner value (excluding the opposite
        # corner since it will be replaced by the corner value).
        # range(left, right) == range(right - left)
        for offset in range(right - left):
            # top == left and bottom == right since matrix is square.
            top, bottom = left, right

            # Save ONLY the top-left value as a temporary variable since we are
            # rotating "backwards"
            top_left = matrix[top][left + offset]

            # Replace the top-left value with the bottom-left value
            matrix[top][left + offset] = matrix[bottom - offset][left]

            # Replace the bottom-left value with the bottom-right value
            matrix[bottom - offset][left] = matrix[bottom][right - offset]

            # Replace the bottom-right value with the top-right value
            matrix[bottom][right - offset] = matrix[top + offset][right]

            # Replace the top-right value with the saved top-left value
            matrix[top + offset][right] = top_left

        left += 1
        right -= 1

    print("\nRotated Matrix:")
    print_matrix(matrix)


def main() -> None:
    """Main function."""
    matrix = [[2, 9, 5, 1], [6, 5, 2, 8], [5, 6, 2, 3], [3, 0, 2, 6]]
    print("Original Matrix:")
    print_matrix(matrix)
    rotate_90_degrees(matrix)


if __name__ == "__main__":
    main()
