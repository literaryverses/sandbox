class Repeat:
    """Print a string a given number of times."""

    # O(n) time complexity
    # O(n) space complexity
    @staticmethod
    def solution(obj, times):
        if times == 0:
            return
        print(obj)
        return Repeat.solution(obj, times - 1)


class Counter:
    """Print 1 to n"""

    # O(n) time complexity
    # O(n) space complexity
    @staticmethod
    def solution(n, current=1):
        if n < current:
            return
        print(current)
        return Counter.solution(n, current + 1)

    # O(n) time complexity
    # O(n) space complexity
    def backtracking(n):
        if n < 1:
            return
        Counter.backtracking(n - 1)
        print(n)  # prints everything after hitting the base case


class CounterBackwards:
    """Print n to 1"""

    @staticmethod
    def solution(n):
        if n < 1:
            return
        print(n)
        return CounterBackwards.solution(n - 1)

    @staticmethod
    def backtracking(n, current=1):
        if n < 0:
            return
        if n < current:
            return
        CounterBackwards.backtracking(n, current + 1)
        print(current)


class Sums:
    pass


class Factorials:
    pass


class Reverse:
    pass


class Palindrome:
    pass


class Fibonacci:
    pass
