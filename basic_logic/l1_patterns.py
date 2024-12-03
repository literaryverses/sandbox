# 1 learn important patterns
from copy import copy


def regular_block(n):
    """
    Prints a square block pattern of asterisks based on the input size.

    Args:
        n (int): The size of the square block.

    Example:
        Input: 3
        Output:
        * * *
        * * *
        * * *
    """
    if n > 0:
        for _ in range(n):
            print("* " * n)


def right_triangle(n):
    """
    Prints a right triangle pattern of asterisks based on the input size.

    Args:
        n (int): The size of the right triangle.

    Example:
        input=5, output=
        *
        * *
        * * *
        * * * *
        * * * * *
    """
    if n > 0:
        for i in range(1, n + 1):
            print("* " * i)


def right_triangle_count_1(n):
    """
    Prints a right triangle pattern of incrementing numbers based on the input size.

    Args:
        n (int): The size of the right triangle.

    Example:
        input=5, output=
        1
        1 2
        1 2 3
        1 2 3 4
        1 2 3 4 5
    """
    if n > 0:
        for row in range(1, n + 1):
            for col in range(1, row + 1):
                if col != row:
                    print(col, end=" ")
                else:
                    print(col)


def right_triangle_count_2(n):
    for i in range(1, n + 1):
        print(" ".join(map(str, range(1, i + 1))))


def right_triangle_integers(n):
    """
    Prints a right triangle pattern of repeated integers based on the input size.

    Args:
        n (int): The size of the right triangle.

    Example:
        input=5, output=
        1
        2 2
        3 3 3
        4 4 4 4
        5 5 5 5 5
    """
    for i in range(1, n + 1):
        print((f"{i} ") * i)


def inverted_right_triangle(n):
    """
    Prints an inverted right triangle pattern of asterisks based on the input size.

    Args:
        n (int): The size of the inverted right triangle.

    Example:
        input=5, output=
        * * * * *
        * * * *
        * * *
        * *
        *
    """
    for i in range(n, 0, -1):
        print("* " * i)


def inverted_right_triangle_count(n):
    """
    Prints an inverted right triangle pattern of incrementing numbers based on the input size.

    Args:
        n (int): The size of the inverted right triangle.

    Example:
        input=5, output=
        1 2 3 4 5
        1 2 3 4
        1 2 3
        1 2
        1
    """
    for i in range(n, 0, -1):
        print(" ".join(map(str, range(1, i + 1))))


def pyramid(n):
    """
    Prints a pyramid pattern of asterisks based on the input size.

    Args:
        n (int): The size of the pyramid.

    Example:
        input=5, output=
            *
           * *
          * * *
         * * * *
        * * * * *
    """
    for i in range(1, n + 1):
        print(" " * (n - i) + "* " * i)


def inverted_pyramid(n):
    """
    Prints an inverted pyramid pattern of asterisks based on the input size.

    Args:
        n (int): The size of the inverted pyramid.

    Example:
        input=5, output=
        * * * * *
         * * * *
          * * *
           * *
            *
    """
    for i in range(n, 0, -1):
        print(" " * (n - i) + "* " * i)


def diamond(n):
    """
    Prints a diamond pattern of asterisks based on the input size.

    Args:
        n (int): The size of the diamond.

    Example:
        input=5, output=
            *
           * *
          * * *
         * * * *
        * * * * *
         * * * *
          * * *
           * *
            *
    """
    for i in range(1, n + 1):
        print(" " * (n - i) + "* " * i)
    for i in range(n - 1, 0, -1):
        print(" " * (n - i) + "* " * i)


def half_diamond(n):
    """
    Prints a half diamond pattern of asterisks based on the input size.

    Args:
        n (int): The size of the half diamond.

    Example:
        input=5, output=
        *
        * *
        * * *
        * * * *
        * * * * *
        * * * *
        * * *
        * *
        *
    """
    for i in range(1, n + 1):
        print("* " * i)
    for i in range(n - 1, 0, -1):
        print("* " * i)


def diamond_filled(n):
    """
    Prints a complete diamond pattern of asterisks based on the input size.

    Args:
        n (int): The size of the complete diamond.

    Example:
        input=5, output=
            *
           ***
          *****
         *******
        *********
         *******
          *****
           ***
            *
    """
    for i in range(1, n + 1):
        print(" " * (n - i) + "*" * (2 * i - 1))
    for i in range(n - 1, 0, -1):
        print(" " * (n - i) + "*" * (2 * i - 1))


def right_triangle_binary_1(n):
    """
    Prints a right triangle pattern of binary numbers based on the input size.

    Args:
        n (int): The size of the right triangle.

    Example:
        input=5, output=
        1
        0 1
        1 0 1
        0 1 0 1
        1 0 1 0 1
    """
    for row in range(1, n + 1):
        if row % 2 == 0:
            num = 0
        else:
            num = 1
        for col in range(1, row + 1):
            if col == row:
                print(num)
            else:
                print(num, end=" ")
            num = 1 - num


def right_triangle_binary_2(n):
    for row in range(1, n + 1):
        rows = []
        for col in range(row):
            rows.append((col + row) % 2)
        print(" ".join(map(str, rows)))


def number_crown(n):
    """
    Prints a crown pattern of numbers based on the input size.

    Args:
        n (int): The size of the crown.

    Example:
        input=5, output=
        1               1
        1 2           2 1
        1 2 3       3 2 1
        1 2 3 4   4 3 2 1
        1 2 3 4 5 4 3 2 1
    """
    max_digit = len(str(n))

    # determine spacing for each row
    rows = [[]] * (max_digit * 2 - 1)
    center = n
    for row in range(max_digit):
        if row == max_digit - 1:
            amount = center
            rows[(len(rows) - 1) // 2] = [" " * (row + 1)] * (2 * amount - 1)
        else:
            amount = 9 * 10**row
            rows[row] = [" " * (row + 1)] * amount
            rows[row - 1] = [" " * (row + 1)] * amount
        center -= 9 * 10**row
    row_template = [item for sublist in rows for item in sublist]

    # determine numbers for each row
    for row in range(1, n + 1):
        row_final = copy(row_template)
        for col in range(1, row + 1):
            row_final[col - 1] = str(col)
            row_final[-col] = str(col)
        print(" ".join(row_final))


def increasing_triangle(n):
    """
    Prints a triangle pattern of increasing numbers based on the input size.

    Args:
        n (int): The size of the triangle.

    Example:
        input=5, output=
        1
        2 3
        4 5 6
        7 8 9 10
        11 12 13 14 15
    """
    count = 1
    for row in range(1, n + 1):
        for col in range(1, row + 1):
            if col == row:
                print(count)
            else:
                print(count, end=" ")
            count += 1


def pyramid_number(n):
    """
    Prints a pyramid pattern of numbers based on the input size.

    Args:
        n (int): The size of the pyramid.

    Example:
        input=5, output=
            1
           121
          12321
         1234321
        123454321
    """
    for row in range(1, n + 1):
        left_side = "".join(str(col % 10) for col in range(1, row + 1))

        right_side = "".join(str(col % 10) for col in range(row - 1, 0, -1))

        print(" " * (n - row) + left_side + right_side)


def right_triangle_count_source(n):
    """
    Prints a right triangle pattern of incrementing numbers from one source
    based on the input size.

    Args:
        n (int): The size of the right triangle.

    Example:
        input=5, output=
        5
        4 5
        3 4 5
        2 3 4 5
        1 2 3 4 5
    """
    for row in range(n):
        for col in range(n - row, n + 1):
            if col != n:
                print(col, end=" ")
            else:
                print(col)


right_triangle_count_source(5)
