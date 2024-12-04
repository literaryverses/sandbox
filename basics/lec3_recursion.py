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
    """Print 1 to n."""

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
    """Print n to 1."""

    # O(n) time complexity
    # O(1) space complexity
    @staticmethod
    def solution(n):
        if n < 1:
            return
        print(n)
        return CounterBackwards.solution(n - 1)

    # O(n) time complexity
    # O(1) space complexity
    @staticmethod
    def backtracking(n, current=1):
        if n < 0:
            return
        if n < current:
            return
        CounterBackwards.backtracking(n, current + 1)
        print(current)


class Sums:
    """Sum of the first n natural numbers."""

    # O(n) time complexity
    # O(1) space complexity
    @staticmethod
    def iterative(n):
        sum = 0
        for i in range(1, n + 1):
            sum += i
        return sum

    # O(1) time complexity
    # O(1) space complexity
    @staticmethod
    def formula(n):
        """arithmetic series"""
        if n < 0:
            return 0
        return n * (n + 1) // 2

    # O(n) time complexity
    # O(n) space complexity
    @staticmethod
    def recursive_parameterized(n, sum=0):
        if n <= 0:
            return sum
        return Sums.recursive_parameterized(n - 1, sum + n)

    # O(n) time complexity
    # O(n) space complexity
    @staticmethod
    def recursive_functional(n):
        if n <= 0:
            return 0
        return n + Sums.recursive_functional(n - 1)


class Factorials:
    """Factorial of a given number."""

    # O(n) time complexity
    # O(1) space complexity
    @staticmethod
    def iterative(n):
        if n < 0:
            raise ValueError("Factorial is not defined for negative numbers.")

        product = 1
        for i in range(1, n + 1):
            product *= i
        return product

    @staticmethod
    # O(n) time complexity
    # O(n) space complexity
    def recursive(n):
        if n < 0:
            raise ValueError("Factorial is not defined for negative numbers.")
        if n == 1:
            return 1
        return n * Factorials.recursive(n - 1)


class ReverseArray:
    """Reverses an array."""


class Palindrome:
    pass


class Fibonacci:
    pass
