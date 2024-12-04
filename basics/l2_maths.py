import math

""""""


class Count_digits:
    """
    Count the number of digits in a given number.
    """

    # O(log n) time complexity
    # O(1) space complexity
    def brute_force(self, n):
        if n == 0:
            return 1
        count = 0
        n = abs(n)
        while n != 0:
            n = n // 10
            count += 1
        return count

    # O(1) time complexity
    # O(1) space complexity
    def optimal_solution(self, n):
        if n == 0:
            return 1
        return int(math.log10(abs(n)) + 1)


class Reverse_number:
    """
    Reverse a given number. Will not include trailing zeroes.
    """

    def optimal_solution(self, n):
        num = abs(n)
        reversed_number = 0
        while num != 0:
            reversed_number = reversed_number * 10 + num % 10
            num = num // 10

        return -reversed_number if n < 0 else reversed_number


class Check_palindrome:
    pass


class GCD_or_HCF:
    pass


class Armstrong_numbers:
    pass


class Print_all_Divisors:
    pass


class Check_for_prime:
    pass
