import unittest
from io import StringIO
import sys
from lec3_recursion import *


class TestRepeat(unittest.TestCase):
    def setUp(self):
        # redirect stdout to capture print statements
        self.held_output = StringIO()
        sys.stdout = self.held_output

    def tearDown(self):
        # reset stdout
        sys.stdout = sys.__stdout__

    def test_basic_functionality(self):
        Repeat.solution("hello", 3)
        self.held_output.seek(0)
        output = self.held_output.read().strip().split("\n")
        self.assertEqual(output, ["hello", "hello", "hello"])

    def test_times_zero(self):
        Repeat.solution("world", 0)
        self.held_output.seek(0)
        output = self.held_output.read()
        self.assertEqual(output, "")

    def test_invalid_times_negative(self):
        with self.assertRaises(RecursionError):
            Repeat.solution("negative", -1)


class TestCounter(unittest.TestCase):
    def setUp(self):
        self.held_output = StringIO()
        sys.stdout = self.held_output

    def tearDown(self):
        sys.stdout = sys.__stdout__

    def test_solution_basic(self):
        Counter.solution(5)
        self.held_output.seek(0)
        output = self.held_output.read().strip().split("\n")
        self.assertEqual(output, ["1", "2", "3", "4", "5"])

    def test_solution_n_zero(self):
        Counter.solution(0)
        self.held_output.seek(0)
        output = self.held_output.read()
        self.assertEqual(output, "")

    def test_solution_negative_n(self):
        Counter.solution(-5)
        self.held_output.seek(0)
        output = self.held_output.read()
        self.assertEqual(output, "")

    def test_solution_large_n(self):
        n = 100
        Counter.solution(n)
        self.held_output.seek(0)
        output = self.held_output.read().strip().split("\n")
        self.assertEqual(output, [str(i) for i in range(1, n + 1)])

    def test_backtracking_basic(self):
        Counter.backtracking(5)
        self.held_output.seek(0)
        output = self.held_output.read().strip().split("\n")
        self.assertEqual(output, ["1", "2", "3", "4", "5"])

    def test_backtracking_n_zero(self):
        Counter.backtracking(0)
        self.held_output.seek(0)
        output = self.held_output.read()
        self.assertEqual(output, "")

    def test_backtracking_negative_n(self):
        Counter.backtracking(-5)
        self.held_output.seek(0)
        output = self.held_output.read()
        self.assertEqual(output, "")

    def test_backtracking_large_n(self):
        n = 100
        Counter.backtracking(n)
        self.held_output.seek(0)
        output = self.held_output.read().strip().split("\n")
        self.assertEqual(output, [str(i) for i in range(1, n + 1)])


class TestCounterBackwards:
    pass


class TestSums:
    pass


class TestFactorials:
    pass


class TestReverse:
    pass


class TestPalindrome:
    pass


class TestFibonacci:
    pass


if __name__ == "__main__":
    unittest.main()
