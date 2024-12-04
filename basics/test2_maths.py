import unittest
from lec2_maths import *


class TestCounter(unittest.TestCase):
    def setUp(self):
        self.counter = Counter()

    def test_single_digit(self):
        self.assertEqual(self.counter.optimal_solution(5), 1)
        self.assertEqual(self.counter.brute_force(5), 1)
        self.assertEqual(self.counter.optimal_solution(9), 1)
        self.assertEqual(self.counter.brute_force(9), 1)

    def test_multiple_digits(self):
        self.assertEqual(self.counter.optimal_solution(10), 2)
        self.assertEqual(self.counter.brute_force(10), 2)
        self.assertEqual(self.counter.optimal_solution(12345), 5)
        self.assertEqual(self.counter.brute_force(12345), 5)
        self.assertEqual(self.counter.optimal_solution(999999), 6)
        self.assertEqual(self.counter.brute_force(999999), 6)

    def test_large_number(self):
        self.assertEqual(self.counter.optimal_solution(1000000000), 10)
        self.assertEqual(self.counter.brute_force(1000000000), 10)

    def test_zero(self):
        self.assertEqual(self.counter.optimal_solution(0), 1)
        self.assertEqual(self.counter.brute_force(0), 1)

    def test_negative_numbers(self):
        self.assertEqual(self.counter.optimal_solution(-7), 1)
        self.assertEqual(self.counter.brute_force(-7), 1)
        self.assertEqual(self.counter.optimal_solution(-12345), 5)
        self.assertEqual(self.counter.brute_force(-12345), 5)


class TestReverser(unittest.TestCase):
    def setUp(self):
        self.reverser = Reverser()

    def test_single_digit(self):
        self.assertEqual(self.reverser.optimal_solution(5), 5)
        self.assertEqual(self.reverser.optimal_solution(-3), -3)

    def test_positive_numbers(self):
        self.assertEqual(self.reverser.optimal_solution(123), 321)
        self.assertEqual(self.reverser.optimal_solution(120), 21)
        self.assertEqual(self.reverser.optimal_solution(1000), 1)

    def test_negative_numbers(self):
        self.assertEqual(self.reverser.optimal_solution(-123), -321)
        self.assertEqual(self.reverser.optimal_solution(-120), -21)
        self.assertEqual(self.reverser.optimal_solution(-1000), -1)

    def test_zero(self):
        self.assertEqual(self.reverser.optimal_solution(0), 0)

    def test_large_numbers(self):
        self.assertEqual(self.reverser.optimal_solution(987654321), 123456789)
        self.assertEqual(self.reverser.optimal_solution(-987654321), -123456789)


class TestPalindrome:
    def setUp(self):
        self.palindrome_checker = Palindrome()

    def test_single_digit(self):
        self.assertTrue(self.palindrome_checker.optimal_solution(5))
        self.assertTrue(self.palindrome_checker.optimal_solution(9))

    def test_palindromes(self):
        self.assertTrue(self.palindrome_checker.optimal_solution(121))
        self.assertTrue(self.palindrome_checker.optimal_solution(12321))
        self.assertTrue(self.palindrome_checker.optimal_solution(1234321))
        self.assertTrue(self.palindrome_checker.optimal_solution(123454321))

    def test_non_palindromes(self):
        self.assertFalse(self.palindrome_checker.optimal_solution(123))
        self.assertFalse(self.palindrome_checker.optimal_solution(1234))
        self.assertFalse(self.palindrome_checker.optimal_solution(12345))
        self.assertFalse(self.palindrome_checker.optimal_solution(123456))

    def test_negative_numbers(self):
        self.assertTrue(self.palindrome_checker.optimal_solution(-121))
        self.assertTrue(self.palindrome_checker.optimal_solution(-12321))
        self.assertTrue(self.palindrome_checker.optimal_solution(-1234321))
        self.assertTrue(self.palindrome_checker.optimal_solution(-123454321))
        self.assertFalse(self.palindrome_checker.optimal_solution(-123))
        self.assertFalse(self.palindrome_checker.optimal_solution(-1234))
        self.assertFalse(self.palindrome_checker.optimal_solution(-12345))
        self.assertFalse(self.palindrome_checker.optimal_solution(-123456))


class TestArmstrongs:
    def setUp(self):
        self.armstrong = Armstrongs()

    def test_armstrong_numbers(self):
        self.assertTrue(self.armstrong.optimal_solution(1))
        self.assertTrue(self.armstrong.optimal_solution(153))
        self.assertTrue(self.armstrong.optimal_solution(370))
        self.assertTrue(self.armstrong.optimal_solution(371))
        self.assertTrue(self.armstrong.optimal_solution(9474))
        self.assertTrue(self.armstrong.optimal_solution(54748))
        self.assertTrue(self.armstrong.optimal_solution(92727))
        self.assertTrue(self.armstrong.optimal_solution(93084))

    def test_non_armstrong_numbers(self):
        self.assertTrue(self.armstrong.optimal_solution(-153))
        self.assertFalse(self.armstrong.optimal_solution(154))
        self.assertFalse(self.armstrong.optimal_solution(3711))
        self.assertFalse(self.armstrong.optimal_solution(9475))
        self.assertFalse(self.armstrong.optimal_solution(54749))
        self.assertFalse(self.armstrong.optimal_solution(92728))
        self.assertFalse(self.armstrong.optimal_solution(93085))


class TestGCDOrHCF:
    def setUp(self):
        self.gcd = GCD_or_HCF()

    def test_gcd(self):
        self.assertEqual(self.gcd.brute_force(10, 5), 5)
        self.assertEqual(self.gcd.optimal_solution(10, 5), 5)
        self.assertEqual(self.gcd.brute_force(14, 28), 14)
        self.assertEqual(self.gcd.optimal_solution(14, 28), 14)
        self.assertEqual(self.gcd.brute_force(15, 25), 5)
        self.assertEqual(self.gcd.optimal_solution(15, 25), 5)
        self.assertEqual(self.gcd.brute_force(100, 200), 100)
        self.assertEqual(self.gcd.optimal_solution(100, 200), 100)
        self.assertEqual(self.gcd.brute_force(1000, 2000), 1000)
        self.assertEqual(self.gcd.optimal_solution(1000, 2000), 1000)
        self.assertEqual(self.gcd.brute_force(10000, 20000), 10000)
        self.assertEqual(self.gcd.optimal_solution(10000, 20000), 10000)
        self.assertEqual(self.gcd.brute_force(15, 27), 3)

    def test_one_gcd(self):
        self.assertEqual(self.gcd.brute_force(10, 3), 1)
        self.assertEqual(self.gcd.optimal_solution(10, 3), 1)
        self.assertEqual(self.gcd.brute_force(14, 15), 1)
        self.assertEqual(self.gcd.optimal_solution(14, 15), 1)
        self.assertEqual(self.gcd.brute_force(100, 201), 1)
        self.assertEqual(self.gcd.optimal_solution(100, 201), 1)
        self.assertEqual(self.gcd.brute_force(1000, 2001), 1)
        self.assertEqual(self.gcd.optimal_solution(1000, 2001), 1)
        self.assertEqual(self.gcd.brute_force(10000, 20001), 1)
        self.assertEqual(self.gcd.optimal_solution(10000, 20001), 1)


class TestPrimes:
    def setUp(self):
        self.primes = Primes()

    def test_primes(self):
        self.assertTrue(self.primes.optimal_solution(2))
        self.assertTrue(self.primes.brute_force(3))
        self.assertTrue(self.primes.optimal_solution(5))
        self.assertTrue(self.primes.brute_force(7))
        self.assertTrue(self.primes.optimal_solution(11))
        self.assertTrue(self.primes.brute_force(13))
        self.assertTrue(self.primes.optimal_solution(17))
        self.assertTrue(self.primes.brute_force(19))
        self.assertTrue(self.primes.optimal_solution(101))
        self.assertTrue(self.primes.brute_force(107))
        self.assertTrue(self.primes.optimal_solution(149))
        self.assertTrue(self.primes.brute_force(157))
        self.assertTrue(self.primes.optimal_solution(167))
        self.assertTrue(self.primes.brute_force(179))

    def test_non_primes(self):
        self.assertFalse(self.primes.optimal_solution(1))
        self.assertFalse(self.primes.brute_force(1))
        self.assertFalse(self.primes.optimal_solution(8))
        self.assertFalse(self.primes.brute_force(9))
        self.assertFalse(self.primes.optimal_solution(10))
        self.assertFalse(self.primes.brute_force(20))
        self.assertFalse(self.primes.optimal_solution(99))
        self.assertFalse(self.primes.brute_force(100))
        self.assertFalse(self.primes.optimal_solution(220))


class TestDivisors:
    def setUp(self):
        self.divisors = Divisors()

    def test_divisors(self):
        self.assertEqual(self.divisors.brute_force(1), {1})
        self.assertEqual(self.divisors.optimal_solution(1), {1})
        self.assertEqual(self.divisors.brute_force(2), {1, 2})
        self.assertEqual(self.divisors.optimal_solution(2), {1, 2})
        self.assertEqual(self.divisors.brute_force(3), {1, 3})
        self.assertEqual(self.divisors.optimal_solution(3), {1, 3})
        self.assertEqual(self.divisors.brute_force(4), {1, 2, 4})
        self.assertEqual(self.divisors.optimal_solution(4), {1, 2, 4})
        self.assertEqual(self.divisors.brute_force(5), {1, 5})
        self.assertEqual(self.divisors.optimal_solution(5), {1, 5})
        self.assertEqual(self.divisors.brute_force(6), {1, 2, 3, 6})
        self.assertEqual(self.divisors.optimal_solution(6), {1, 2, 3, 6})
        self.assertEqual(self.divisors.brute_force(7), {1, 7})
        self.assertEqual(self.divisors.optimal_solution(7), {1, 7})
        self.assertEqual(self.divisors.brute_force(8), {1, 2, 4, 8})
        self.assertEqual(self.divisors.optimal_solution(8), {1, 2, 4, 8})
        self.assertEqual(self.divisors.brute_force(9), {1, 3, 9})
        self.assertEqual(self.divisors.optimal_solution(9), {1, 3, 9})
        self.assertEqual(self.divisors.brute_force(10), {1, 2, 5, 10})
        self.assertEqual(self.divisors.optimal_solution(10), {1, 2, 5, 10})

    def test_negative_numbers(self):
        self.assertEqual(self.divisors.brute_force(-1), {1, -1})
        self.assertEqual(self.divisors.optimal_solution(-1), {1, -1})
        self.assertEqual(self.divisors.brute_force(-2), {1, 2, -2, -1})
        self.assertEqual(self.divisors.optimal_solution(-15), {1, 3, 5, 15, -1, -3, -5})


if __name__ == "__main__":
    unittest.main()
