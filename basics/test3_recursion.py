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

    def test_solution_zero(self):
        Counter.solution(0)
        self.held_output.seek(0)
        output = self.held_output.read()
        self.assertEqual(output, "")

    def test_solution_negative(self):
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

    def test_backtracking_zero(self):
        Counter.backtracking(0)
        self.held_output.seek(0)
        output = self.held_output.read()
        self.assertEqual(output, "")

    def test_backtracking_negative(self):
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


class TestCounterBackwards(unittest.TestCase):
    def setUp(self):
        self.held_output = StringIO()
        sys.stdout = self.held_output

    def tearDown(self):
        sys.stdout = sys.__stdout__

    def test_solution_basic(self):
        CounterBackwards.solution(5)
        self.held_output.seek(0)
        output = self.held_output.read().strip().split("\n")
        self.assertEqual(output, ["5", "4", "3", "2", "1"])

    def test_solution_zero(self):
        CounterBackwards.solution(0)
        self.held_output.seek(0)
        output = self.held_output.read()
        self.assertEqual(output, "")

    def test_solution_negative(self):
        CounterBackwards.solution(-5)
        self.held_output.seek(0)
        output = self.held_output.read()
        self.assertEqual(output, "")

    def test_solution_large(self):
        n = 100
        CounterBackwards.solution(n)
        self.held_output.seek(0)
        output = self.held_output.read().strip().split("\n")
        self.assertEqual(output, [str(i) for i in range(n, 0, -1)])

    def test_backtracking_basic(self):
        CounterBackwards.backtracking(5)
        self.held_output.seek(0)
        output = self.held_output.read().strip().split("\n")
        self.assertEqual(output, ["5", "4", "3", "2", "1"])

    def test_backtracking_zero(self):
        CounterBackwards.backtracking(0)
        self.held_output.seek(0)
        output = self.held_output.read()
        self.assertEqual(output, "")

    def test_backtracking_negative(self):
        CounterBackwards.backtracking(-5)
        self.held_output.seek(0)
        output = self.held_output.read()
        self.assertEqual(output, "")

    def test_backtracking_large(self):
        n = 100
        CounterBackwards.backtracking(n)
        self.held_output.seek(0)
        output = self.held_output.read().strip().split("\n")
        self.assertEqual(output, [str(i) for i in range(n, 0, -1)])


class TestSums(unittest.TestCase):
    def test_loop_basic(self):
        self.assertEqual(Sums.iterative(5), 15)
        self.assertEqual(Sums.iterative(10), 55)

    def test_loop_zero(self):
        self.assertEqual(Sums.iterative(0), 0)

    def test_loop_negative(self):
        self.assertEqual(Sums.iterative(-5), 0)

    def test_formula_basic(self):
        self.assertEqual(Sums.formula(5), 15)
        self.assertEqual(Sums.formula(10), 55)

    def test_formula_zero(self):
        self.assertEqual(Sums.formula(0), 0)

    def test_formula_negative(self):
        self.assertEqual(Sums.formula(-5), 0)

    def test_recursive_parameterized_basic(self):
        self.assertEqual(Sums.recursive_parameterized(5), 15)
        self.assertEqual(Sums.recursive_parameterized(10), 55)

    def test_recursive_parameterized_zero(self):
        self.assertEqual(Sums.recursive_parameterized(0), 0)

    def test_recursive_parameterized_negative(self):
        self.assertEqual(Sums.recursive_parameterized(-5), 0)

    def test_recursive_functional_basic(self):
        self.assertEqual(Sums.recursive_functional(5), 15)
        self.assertEqual(Sums.recursive_functional(10), 55)

    def test_recursive_functional_zero(self):
        self.assertEqual(Sums.recursive_functional(0), 0)

    def test_recursive_functional_negative(self):
        self.assertEqual(Sums.recursive_functional(-5), 0)

    def test_large_n(self):
        n = 100
        expected = n * (n + 1) // 2
        self.assertEqual(Sums.iterative(n), expected)
        self.assertEqual(Sums.formula(n), expected)
        self.assertEqual(Sums.recursive_parameterized(n), expected)
        self.assertEqual(Sums.recursive_functional(n), expected)


class TestFactorials(unittest.TestCase):
    def test_iterative_basic(self):
        self.assertEqual(Factorials.iterative(5), 120)
        self.assertEqual(Factorials.iterative(10), 3628800)

    def test_iterative_one(self):
        self.assertEqual(Factorials.iterative(1), 1)

    def test_iterative_zero(self):
        self.assertEqual(Factorials.iterative(0), 1)

    def test_iterative_negative(self):
        with self.assertRaises(ValueError):
            Factorials.iterative(-5)

    def test_recursive_basic(self):
        self.assertEqual(Factorials.recursive(5), 120)
        self.assertEqual(Factorials.recursive(10), 3628800)

    def test_recursive_one(self):
        self.assertEqual(Factorials.recursive(1), 1)

    def test_recursive_zero(self):
        with self.assertRaises(ValueError):
            Factorials.recursive(0)

    def test_recursive_negative(self):
        with self.assertRaises(ValueError):
            Factorials.recursive(-5)

    def test_large(self):
        n = 200
        expected = 1
        for i in range(1, n + 1):
            expected *= i
        self.assertEqual(Factorials.iterative(n), expected)
        self.assertEqual(Factorials.recursive(n), expected)


class TestReverseArray(unittest.TestCase):
    def test_iterative_basic(self):
        array = [1, 2, 3, 4, 5]
        result = ReverseArray.iterative(array)
        self.assertEqual(result, [5, 4, 3, 2, 1])

    def test_iterative_empty(self):
        array = []
        result = ReverseArray.iterative(array)
        self.assertEqual(result, [])

    def test_iterative_single_element(self):
        array = [1]
        result = ReverseArray.iterative(array)
        self.assertEqual(result, [1])

    def test_two_pointers_basic(self):
        array = [1, 2, 3, 4, 5]
        result = ReverseArray.two_pointers(array)
        self.assertEqual(result, [5, 4, 3, 2, 1])

    def test_two_pointers_empty(self):
        array = []
        result = ReverseArray.two_pointers(array)
        self.assertEqual(result, [])

    def test_two_pointers_single_element(self):
        array = [1]
        result = ReverseArray.two_pointers(array)
        self.assertEqual(result, [1])

    def test_recursive_basic(self):
        array = [1, 2, 3, 4, 5]
        result = ReverseArray.recursive(array)
        self.assertEqual(result, [5, 4, 3, 2, 1])

    def test_recursive_empty(self):
        array = []
        result = ReverseArray.recursive(array)
        self.assertEqual(result, [])

    def test_recursive_single_element(self):
        array = [1]
        result = ReverseArray.recursive(array)
        self.assertEqual(result, [1])

    def test_stress_test(self):
        array = list(range(1, 1001))
        result = ReverseArray.iterative(array)
        self.assertEqual(result, list(range(1000, 0, -1)))

        array = list(range(1, 1001))
        result = ReverseArray.two_pointers(array)
        self.assertEqual(result, list(range(1000, 0, -1)))

        array = list(range(1, 1001))
        result = ReverseArray.recursive(array)
        self.assertEqual(result, list(range(1000, 0, -1)))


class TestPalindrome(unittest.TestCase):
    pass


class TestFibonacci(unittest.TestCase):
    pass


if __name__ == "__main__":
    unittest.main()
