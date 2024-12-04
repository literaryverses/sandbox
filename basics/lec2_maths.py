import math

""""""


class Count_digits:
    """
    Count the number of digits in a given number.
    """

    # O(log n) time complexity
    # O(1) space complexity
    @staticmethod
    def brute_force(n):
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
    @staticmethod
    def optimal_solution(n):
        if n == 0:
            return 1
        return int(math.log10(abs(n)) + 1)


class Reverse_number:
    """
    Reverse a given number. Will not include trailing zeroes.
    """

    # O(log n) time complexity
    # O(1) space complexity
    @staticmethod
    def optimal_solution(n):
        num = abs(n)
        reversed_number = 0
        while num != 0:
            reversed_number = reversed_number * 10 + num % 10
            num = num // 10

        return -reversed_number if n < 0 else reversed_number


class Check_palindrome:
    """
    Check if a given number is a palindrome.
    """

    @staticmethod
    def optimal_solution(n):
        reversed_number = Reverse_number.optimal_solution(n)
        if n == reversed_number:
            return True
        else:
            return False


class GCD_or_HCF:
    """
    Find the Greatest Common Divisor (GCD) or Highest Common Factor (HCF) of two numbers.
    """

    # O(n) time complexity
    # O(1) space complexity
    @staticmethod
    def brute_force(num1, num2):
        min = min(num1, num2)
        for i in range(min, 0, -1):
            if num1 % i == 0 and num2 % i == 0:
                return i
        return "No GCD/HCF found"

    # O(log n) time complexity
    # O(1) space complexity
    @staticmethod
    def optimal_solution(num1, num2):
        """Uses Euclid's algorithim"""
        while num1 != 0 and num2 != 0:
            num1, num2 = min(num1, num2), max(num1, num2)
            num2 -= num1
        return max(num1, num2)


class Armstrong_numbers:
    """
    Check if a number is a Armstrong number.
    Amrstrong number is a number that is equalto the sum of its own digits each raised
    to the power of the number of digits.
    """

    @staticmethod
    def optimal_solution(n):
        if n < 0:
            return False

        num_of_digits = Count_digits.optimal_solution(n)
        sum_of_digits = 0
        temp = n
        while temp != 0:
            digit = temp % 10
            sum_of_digits += digit**num_of_digits
            temp = temp // 10

        return n == sum_of_digits


class Print_all_Divisors:
    pass


class Check_for_prime:
    pass
