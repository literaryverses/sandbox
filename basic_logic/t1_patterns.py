import unittest
from io import StringIO
from unittest.mock import patch
from l1_patterns import (
    regular_block,
    right_triangle,
    right_triangle_integers_2,
    right_triangle_integers_1,
)


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


class TestRightTriangleIntegers(unittest.TestCase):
    @patch("sys.stdout", new_callable=StringIO)
    def test_right_triangle_positive(self, mock_stdout):
        input_value = 5

        right_triangle_integers_1(input_value)
        output_1 = mock_stdout.getvalue()

        mock_stdout.truncate(0)
        mock_stdout.seek(0)

        right_triangle_integers_2(input_value)
        output_2 = mock_stdout.getvalue()

        expected_output = "1\n1 2\n1 2 3\n1 2 3 4\n1 2 3 4 5\n"
        self.assertTrue(output_1 == output_2 == expected_output)

    @patch("sys.stdout", new_callable=StringIO)
    def test_right_triangle_zero(self, mock_stdout):
        input_value = 0

        right_triangle_integers_1(input_value)
        output_1 = mock_stdout.getvalue()

        mock_stdout.truncate(0)
        mock_stdout.seek(0)

        right_triangle_integers_2(input_value)
        output_2 = mock_stdout.getvalue()

        self.assertTrue(output_1 == output_2 == "")

    @patch("sys.stdout", new_callable=StringIO)
    def test_right_triangle_one(self, mock_stdout):
        input_value = 1

        right_triangle_integers_1(input_value)
        output_1 = mock_stdout.getvalue()

        mock_stdout.truncate(0)
        mock_stdout.seek(0)

        right_triangle_integers_2(input_value)
        output_2 = mock_stdout.getvalue()

        expected_output = "1\n"

        self.assertTrue(output_1 == output_2 == expected_output)

    @patch("sys.stdout", new_callable=StringIO)
    def test_right_triangle_negative(self, mock_stdout):
        input_value = -5

        right_triangle_integers_1(input_value)
        output_1 = mock_stdout.getvalue()

        mock_stdout.truncate(0)
        mock_stdout.seek(0)

        right_triangle_integers_2(input_value)
        output_2 = mock_stdout.getvalue()

        self.assertTrue(output_1 == output_2 == "")


if __name__ == "__main__":
    unittest.main()
