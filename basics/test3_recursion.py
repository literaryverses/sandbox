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
        Repeat.recursive("hello", 3)
        self.held_output.seek(0)
        output = self.held_output.read().strip().split("\n")
        self.assertEqual(output, ["hello", "hello", "hello"])

    def test_times_zero(self):
        Repeat.recursive("world", 0)
        self.held_output.seek(0)
        output = self.held_output.read()
        self.assertEqual(output, "")

    def test_invalid_times_negative(self):
        with self.assertRaises(RecursionError):
            Repeat.recursive("negative", -1)


class TestCounter(unittest.TestCase):
    def setUp(self):
        self.held_output = StringIO()
        sys.stdout = self.held_output

    def tearDown(self):
        sys.stdout = sys.__stdout__

    def test_recursive_basic(self):
        Counter.recursive_basic(5)
        self.held_output.seek(0)
        output = self.held_output.read().strip().split("\n")
        self.assertEqual(output, ["1", "2", "3", "4", "5"])

    def test_recursive_zero(self):
        Counter.recursive_basic(0)
        self.held_output.seek(0)
        output = self.held_output.read()
        self.assertEqual(output, "")

    def test_recursive_negative(self):
        Counter.recursive_basic(-5)
        self.held_output.seek(0)
        output = self.held_output.read()
        self.assertEqual(output, "")

    def test_recursive_large_n(self):
        n = 100
        Counter.recursive_basic(n)
        self.held_output.seek(0)
        output = self.held_output.read().strip().split("\n")
        self.assertEqual(output, [str(i) for i in range(1, n + 1)])

    def test_backtracking_basic(self):
        Counter.recursive_backtracking(5)
        self.held_output.seek(0)
        output = self.held_output.read().strip().split("\n")
        self.assertEqual(output, ["1", "2", "3", "4", "5"])

    def test_backtracking_zero(self):
        Counter.recursive_backtracking(0)
        self.held_output.seek(0)
        output = self.held_output.read()
        self.assertEqual(output, "")

    def test_backtracking_negative(self):
        Counter.recursive_backtracking(-5)
        self.held_output.seek(0)
        output = self.held_output.read()
        self.assertEqual(output, "")

    def test_backtracking_large_n(self):
        n = 100
        Counter.recursive_backtracking(n)
        self.held_output.seek(0)
        output = self.held_output.read().strip().split("\n")
        self.assertEqual(output, [str(i) for i in range(1, n + 1)])


class TestCounterBackwards(unittest.TestCase):
    def setUp(self):
        self.held_output = StringIO()
        sys.stdout = self.held_output

    def tearDown(self):
        sys.stdout = sys.__stdout__

    def test_recursive_basic(self):
        CounterBackwards.recursive_basic(5)
        self.held_output.seek(0)
        output = self.held_output.read().strip().split("\n")
        self.assertEqual(output, ["5", "4", "3", "2", "1"])

    def test_recursive_zero(self):
        CounterBackwards.recursive_basic(0)
        self.held_output.seek(0)
        output = self.held_output.read()
        self.assertEqual(output, "")

    def test_recursive_negative(self):
        CounterBackwards.recursive_basic(-5)
        self.held_output.seek(0)
        output = self.held_output.read()
        self.assertEqual(output, "")

    def test_recursive_large(self):
        n = 100
        CounterBackwards.recursive_basic(n)
        self.held_output.seek(0)
        output = self.held_output.read().strip().split("\n")
        self.assertEqual(output, [str(i) for i in range(n, 0, -1)])

    def test_backtracking_basic(self):
        CounterBackwards.recursive_backtracking(5)
        self.held_output.seek(0)
        output = self.held_output.read().strip().split("\n")
        self.assertEqual(output, ["5", "4", "3", "2", "1"])

    def test_backtracking_zero(self):
        CounterBackwards.recursive_backtracking(0)
        self.held_output.seek(0)
        output = self.held_output.read()
        self.assertEqual(output, "")

    def test_backtracking_negative(self):
        CounterBackwards.recursive_backtracking(-5)
        self.held_output.seek(0)
        output = self.held_output.read()
        self.assertEqual(output, "")

    def test_backtracking_large(self):
        n = 100
        CounterBackwards.recursive_backtracking(n)
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
    def test_two_pointer_basic(self):
        self.assertTrue(Palindrome.two_pointer("racecar"))
        self.assertTrue(Palindrome.two_pointer("madam"))
        self.assertFalse(Palindrome.two_pointer("hello"))

    def test_two_pointer_empty(self):
        self.assertTrue(Palindrome.two_pointer(""))

    def test_two_pointer_single_character(self):
        self.assertTrue(Palindrome.two_pointer("a"))

    def test_two_pointer_case_sensitive(self):
        self.assertFalse(Palindrome.two_pointer("Racecar"))

    def test_recursive_basic(self):
        self.assertTrue(Palindrome.recursive("racecar"))
        self.assertTrue(Palindrome.recursive("madam"))
        self.assertFalse(Palindrome.recursive("hello"))

    def test_recursive_empty(self):
        self.assertTrue(Palindrome.recursive(""))

    def test_recursive_single_character(self):
        self.assertTrue(Palindrome.recursive("a"))

    def test_recursive_case_sensitive(self):
        self.assertFalse(Palindrome.recursive("Racecar"))

    def test_stress_test(self):
        long_palindrome = "a" * 900 + "b" + "a" * 900
        self.assertTrue(Palindrome.two_pointer(long_palindrome))
        self.assertTrue(Palindrome.recursive(long_palindrome))

        long_non_palindrome = "a" * 900 + "b" + "c" + "a" * 899
        self.assertFalse(Palindrome.two_pointer(long_non_palindrome))
        self.assertFalse(Palindrome.recursive(long_non_palindrome))


class TestFibonacci(unittest.TestCase):
    def test_two_pointers_basic(self):
        self.assertEqual(Fibonacci.two_pointers(0), [])
        self.assertEqual(Fibonacci.two_pointers(1), [0])
        self.assertEqual(Fibonacci.two_pointers(2), [0, 1])
        self.assertEqual(Fibonacci.two_pointers(5), [0, 1, 1, 2, 3])
        self.assertEqual(Fibonacci.two_pointers(10), [0, 1, 1, 2, 3, 5, 8, 13, 21, 34])

    def test_recursive_basic(self):
        self.assertEqual(Fibonacci.recursive(0), [])
        self.assertEqual(Fibonacci.recursive(1), [0])
        self.assertEqual(Fibonacci.recursive(2), [0, 1])
        self.assertEqual(Fibonacci.recursive(5), [0, 1, 1, 2, 3])
        self.assertEqual(Fibonacci.recursive(10), [0, 1, 1, 2, 3, 5, 8, 13, 21, 34])

    def test_large_inputs(self):
        self.assertEqual(Fibonacci.two_pointers(15), Fibonacci.recursive(15))
        self.assertEqual(Fibonacci.two_pointers(20), Fibonacci.recursive(20))

    def test_edge_cases(self):
        self.assertEqual(Fibonacci.two_pointers(-5), [])
        self.assertEqual(Fibonacci.recursive(-5), [])
        self.assertEqual(Fibonacci.two_pointers(0), [])
        self.assertEqual(Fibonacci.recursive(0), [])


if __name__ == "__main__":
    unittest.main()
