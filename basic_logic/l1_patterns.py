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


""" input=5, output=
*
* *
* * *
* * * *
* * * * *"""


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


def right_triangle_integers_1(n):
    """
    Prints a right triangle pattern of numbers based on the input size.

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


def right_triangle_integers_2(n):
    for row in range(1, n + 1):
        print(" ".join(map(str, range(1, row + 1))))
