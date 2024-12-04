import unittest
from l2_maths import *


class TestCountDigits(unittest.TestCase):
    def setUp(self):
        self.counter = Count_digits()

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


class TestOptimalSolution(unittest.TestCase):
    def setUp(self):
        self.reverser = Reverse_number()

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


if __name__ == "__main__":
    unittest.main()