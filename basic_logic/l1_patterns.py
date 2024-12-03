# 1 learn important patterns


""" input=3, output=
* * *
* * *
* * *"""


def regular_block(n):
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
    if n > 0:
        for i in range(1, n + 1):
            print("* " * i)
