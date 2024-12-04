class Repeat:
    """Print a string a given number of times."""

    # O(n) time complexity
    # O(n) space complexity
    @staticmethod
    def solution(word, times):
        if times == 0:
            return
        print(word)
        return Repeat.solution(word, times - 1)


class Counter:
    """Print a string backwards."""

    @staticmethod
    def solution(word):
        if word == "":
            return


class CounterBackwards:
    pass


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
