import math


class Count_digits:
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
    pass


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
