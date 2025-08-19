"""
Pascal's Triangle Generator
---------------------------
Author: Dharani Manchala
Date: 2025-08-09
Description:
    This program generates Pascal's Triangle up to a specified number of rows.

    Pascal's Triangle is a triangular array of numbers in which each number
    is the sum of the two numbers directly above it.

Example:
    For 5 rows:
        1
        1 1
        1 2 1
        1 3 3 1
        1 4 6 4 1
"""

def generate_pascals_triangle(n_rows):
    """
    Generate Pascal's Triangle up to n_rows.

    Args:
        n_rows (int): Number of rows to generate.

    Returns:
        list[list[int]]: 2D list containing Pascal's Triangle numbers.
    """
    triangle = []

    for row in range(n_rows):
        # Start each row with 1
        current_row = [1]

        if triangle:  # From second row onward
            last_row = triangle[-1]
            # Each middle element is sum of two numbers above it
            for i in range(len(last_row) - 1):
                current_row.append(last_row[i] + last_row[i + 1])
            # End each row with 1
            current_row.append(1)

        triangle.append(current_row)

    return triangle


def print_pascals_triangle(triangle):
    """
    Print Pascal's Triangle in a formatted way.

    Args:
        triangle (list[list[int]]): Pascal's Triangle data.
    """
    max_width = len(" ".join(map(str, triangle[-1])))  # Width for alignment
    for row in triangle:
        print(" ".join(map(str, row)).center(max_width))


if __name__ == "__main__":
    # Number of rows for the triangle
    try:
        rows = int(input("Enter the number of rows for Pascal's Triangle: "))
        if rows <= 0:
            raise ValueError("Number of rows must be positive.")
        
        pascal = generate_pascals_triangle(rows)
        print("\nPascal's Triangle:")
        print_pascals_triangle(pascal)

    except ValueError as e:
        print(f"Invalid input: {e}")
