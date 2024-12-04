import unittest
from io import StringIO
import sys
from lec3_recursion import *


class TestRepeat:
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

    def test_invalid_word_type(self):
        with self.assertRaises(AttributeError):
            Repeat.solution(123, 3)


class TestCounter:
    pass


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
