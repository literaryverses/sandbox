import unittest
from io import StringIO
from unittest.mock import patch
from basic_logic.l1_patterns import regular_block, right_triangle


class TestRegularBlock(unittest.TestCase):
    @patch("sys.stdout", new_callable=StringIO)
    def test_regular_block_positive(self, mock_stdout):
        regular_block(3)
        expected_output = "* * * \n" "* * * \n" "* * * \n"
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch("sys.stdout", new_callable=StringIO)
    def test_regular_block_zero(self, mock_stdout):
        regular_block(0)
        self.assertEqual(mock_stdout.getvalue(), "")

    @patch("sys.stdout", new_callable=StringIO)
    def test_regular_block_one(self, mock_stdout):
        regular_block(1)
        expected_output = "* \n"
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch("sys.stdout", new_callable=StringIO)
    def test_regular_block_negative(self, mock_stdout):
        regular_block(-5)
        self.assertEqual(mock_stdout.getvalue(), "")


class TestRightTriange(unittest.TestCase):
    @patch("sys.stdout", new_callable=StringIO)
    def test_right_triangle_positive(self, mock_stdout):
        right_triangle(5)
        expected_output = "* \n" "* * \n" "* * * \n" "* * * * \n" "* * * * * \n"
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch("sys.stdout", new_callable=StringIO)
    def test_right_triangle_zero(self, mock_stdout):
        right_triangle(0)
        self.assertEqual(mock_stdout.getvalue(), "")

    @patch("sys.stdout", new_callable=StringIO)
    def test_right_triangle_one(self, mock_stdout):
        right_triangle(1)
        expected_output = "* \n"
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch("sys.stdout", new_callable=StringIO)
    def test_right_triangle_negative(self, mock_stdout):
        right_triangle(-5)
        self.assertEqual(mock_stdout.getvalue(), "")


if __name__ == "__main__":
    unittest.main()
