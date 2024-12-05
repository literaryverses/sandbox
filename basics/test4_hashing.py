import unittest
from lec4_hashing import *


class TestHashingBasics(unittest.TestCase):
    def setUp(self):
        self.array = ["a", "b", "a", "c", "b", "a"]
        self.queries = {"a", "b", "d"}
        self.expected_result = {"a": 3, "b": 2, "d": 0}
        self.hashing_basics = HashingBasics(self.array)

    def test_brute_force(self):
        result = self.hashing_basics.brute_force(self.queries)
        self.assertEqual(result, self.expected_result)

    def test_hashing(self):
        result = self.hashing_basics.hashing(self.queries)
        self.assertEqual(result, self.expected_result)

    def test_large_input(self):
        large_array = ["x"] * 1000 + ["y"] * 2000 + ["z"] * 3000
        large_queries = {"x", "y", "z", "a"}
        expected_large_result = {"x": 1000, "y": 2000, "z": 3000, "a": 0}
        large_hashing_basics = HashingBasics(large_array)

        result_brute = large_hashing_basics.brute_force(large_queries)
        self.assertEqual(result_brute, expected_large_result)

        result_hashing = large_hashing_basics.hashing(large_queries)
        self.assertEqual(result_hashing, expected_large_result)


class TestFrequencies(unittest.TestCase):
    def test_getFreqs_basic(self):
        array = ["a", "b", "a", "c", "b", "a"]
        freqs = Frequencies(array).getFreqs()
        expected = {"a": 3, "b": 2, "c": 1}
        self.assertEqual(freqs, expected)

        array = []
        freqs = Frequencies(array).getFreqs()
        expected = {}
        self.assertEqual(freqs, expected)

        array = [1, 2, 1, 3, 2, 2, 3]
        freqs = Frequencies(array).getFreqs()
        expected = {1: 2, 2: 3, 3: 2}
        self.assertEqual(freqs, expected)

    def test_getMinMaxFreqs_basic(self):
        array = ["a", "b", "a", "c", "b", "a"]
        max_freq, min_freq = Frequencies(array).getMinMaxFreqs()
        self.assertEqual(max_freq, ("a", 3))
        self.assertEqual(min_freq, ("c", 1))

        array = []
        max_freq, min_freq = Frequencies(array).getMinMaxFreqs()
        self.assertEqual(max_freq, None)
        self.assertEqual(min_freq, None)

        array = [1, 2, 3, 2, 3, 1]
        max_freq, min_freq = Frequencies(array).getMinMaxFreqs()
        self.assertIn(max_freq, [(1, 2), (2, 2), (3, 2)])
        self.assertIn(min_freq, [(1, 2), (2, 2), (3, 2)])

    def test_edge_cases(self):
        array = ["a"]
        max_freq, min_freq = Frequencies(array).getMinMaxFreqs()
        self.assertEqual(max_freq, ("a", 1))
        self.assertEqual(min_freq, ("a", 1))

        array = ["x", "x", "x", "x"]
        max_freq, min_freq = Frequencies(array).getMinMaxFreqs()
        self.assertEqual(max_freq, ("x", 4))
        self.assertEqual(min_freq, ("x", 4))


if __name__ == "__main__":
    unittest.main()
