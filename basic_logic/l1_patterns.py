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
    for i in range(1, n + 1):
        if i % 2 == 0:
            num = 0
        else:
            num = 1
        for j in range(1, i + 1):
            if j == i:
                print(num)
            else:
                print(num, end=" ")
            num = 1 - num


def right_triangle_binary_2(n):
    for i in range(1, n + 1):
        row = []
        for j in range(i):
            row.append((j + i) % 2)
        print(" ".join(map(str, row)))


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
    row = [[]] * (max_digit * 2 - 1)
    center = n
    for i in range(max_digit):
        if i == max_digit - 1:
            amount = center
            row[(len(row) - 1) // 2] = [" " * (i + 1)] * (2 * amount - 1)
        else:
            amount = 9 * 10**i
            row[i] = [" " * (i + 1)] * amount
            row[i - 1] = [" " * (i + 1)] * amount
        center -= 9 * 10**i
    row_template = [item for sublist in row for item in sublist]

    # determine numbers for each row
    for i in range(1, n + 1):
        row = copy(row_template)
        for j in range(1, i + 1):
            row[j - 1] = str(j)
            row[-j] = str(j)
        print(" ".join(row))


number_crown(11)
