# 1 learn important patterns


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
        for col in range(1, n + 1):
            print("* " * col)


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
    for col in range(1, n + 1):
        print(" ".join(map(str, range(1, col + 1))))


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
    for count in range(1, n + 1):
        print((f"{count} ") * count)


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
    for col in range(n, 0, -1):
        print("* " * col)


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
    for col in range(n, 0, -1):
        print(" ".join(map(str, range(1, col + 1))))


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
    for row in range(1, n + 1):
        print(" " * (n - row) + "* " * row)


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
    for row in range(n, 0, -1):
        print(" " * (n - row) + "* " * row)


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
    pass


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
    pass


def right_triangle_binary(n):
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
    pass
