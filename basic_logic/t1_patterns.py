import unittest
from io import StringIO
from unittest.mock import patch
from l1_patterns import *


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

        right_triangle_count_1(input_value)
        output_1 = mock_stdout.getvalue()

        mock_stdout.truncate(0)
        mock_stdout.seek(0)

        right_triangle_count_2(input_value)
        output_2 = mock_stdout.getvalue()

        expected_output = "1\n1 2\n1 2 3\n1 2 3 4\n1 2 3 4 5\n"
        self.assertTrue(output_1 == output_2 == expected_output)

    @patch("sys.stdout", new_callable=StringIO)
    def test_right_triangle_zero(self, mock_stdout):
        input_value = 0

        right_triangle_count_1(input_value)
        output_1 = mock_stdout.getvalue()

        mock_stdout.truncate(0)
        mock_stdout.seek(0)

        right_triangle_count_2(input_value)
        output_2 = mock_stdout.getvalue()

        self.assertTrue(output_1 == output_2 == "")

    @patch("sys.stdout", new_callable=StringIO)
    def test_right_triangle_one(self, mock_stdout):
        input_value = 1

        right_triangle_count_1(input_value)
        output_1 = mock_stdout.getvalue()

        mock_stdout.truncate(0)
        mock_stdout.seek(0)

        right_triangle_count_2(input_value)
        output_2 = mock_stdout.getvalue()

        expected_output = "1\n"

        self.assertTrue(output_1 == output_2 == expected_output)

    @patch("sys.stdout", new_callable=StringIO)
    def test_right_triangle_negative(self, mock_stdout):
        input_value = -5

        right_triangle_count_1(input_value)
        output_1 = mock_stdout.getvalue()

        mock_stdout.truncate(0)
        mock_stdout.seek(0)

        right_triangle_count_2(input_value)
        output_2 = mock_stdout.getvalue()

        self.assertTrue(output_1 == output_2 == "")


class TestRightTriangleIntegers(unittest.TestCase):
    @patch("sys.stdout", new_callable=StringIO)
    def test_right_triangle_positive(self, mock_stdout):
        right_triangle_integers(5)
        expected_output = "1 \n2 2 \n3 3 3 \n4 4 4 4 \n5 5 5 5 5 \n"
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch("sys.stdout", new_callable=StringIO)
    def test_right_triangle_zero(self, mock_stdout):
        right_triangle_integers(0)
        self.assertEqual(mock_stdout.getvalue(), "")

    @patch("sys.stdout", new_callable=StringIO)
    def test_right_triangle_one(self, mock_stdout):
        right_triangle_integers(1)
        expected_output = "1 \n"
        self.assertEqual(mock_stdout.getvalue(), expected_output)


class TestInvertedRightTriangle(unittest.TestCase):
    @patch("sys.stdout", new_callable=StringIO)
    def test_inverted_right_triangle_positive(self, mock_stdout):
        inverted_right_triangle(5)
        expected_output = "* * * * * \n* * * * \n* * * \n* * \n* \n"
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch("sys.stdout", new_callable=StringIO)
    def test_inverted_right_triangle_zero(self, mock_stdout):
        inverted_right_triangle(0)
        self.assertEqual(mock_stdout.getvalue(), "")

    @patch("sys.stdout", new_callable=StringIO)
    def test_inverted_right_triangle_one(self, mock_stdout):
        inverted_right_triangle(1)
        expected_output = "* \n"
        self.assertEqual(mock_stdout.getvalue(), expected_output)


class TestInvertedRightTriangleCount(unittest.TestCase):
    @patch("sys.stdout", new_callable=StringIO)
    def test_inverted_right_triangle_count_positive(self, mock_stdout):
        inverted_right_triangle_count(5)
        expected_output = "1 2 3 4 5\n1 2 3 4\n1 2 3\n1 2\n1\n"
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch("sys.stdout", new_callable=StringIO)
    def test_inverted_right_triangle_count_zero(self, mock_stdout):
        inverted_right_triangle_count(0)
        self.assertEqual(mock_stdout.getvalue(), "")

    @patch("sys.stdout", new_callable=StringIO)
    def test_inverted_right_triangle_count_one(self, mock_stdout):
        inverted_right_triangle_count(1)
        expected_output = "1\n"
        self.assertEqual(mock_stdout.getvalue(), expected_output)


class TestPyramid(unittest.TestCase):
    @patch("sys.stdout", new_callable=StringIO)
    def test_pyramid_positive(self, mock_stdout):
        pyramid(5)
        expected_output = "    * \n   * * \n  * * * \n * * * * \n* * * * * \n"
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch("sys.stdout", new_callable=StringIO)
    def test_pyramid_zero(self, mock_stdout):
        pyramid(0)
        self.assertEqual(mock_stdout.getvalue(), "")

    @patch("sys.stdout", new_callable=StringIO)
    def test_pyramid_one(self, mock_stdout):
        pyramid(1)
        expected_output = "* \n"
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch("sys.stdout", new_callable=StringIO)
    def test_pyramid_negative(self, mock_stdout):
        pyramid(-5)
        self.assertEqual(mock_stdout.getvalue(), "")


class TestInvertedPyramid(unittest.TestCase):
    @patch("sys.stdout", new_callable=StringIO)
    def test_inverted_pyramid_positive(self, mock_stdout):
        inverted_pyramid(5)
        expected_output = "* * * * * \n * * * * \n  * * * \n   * * \n    * \n"
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch("sys.stdout", new_callable=StringIO)
    def test_inverted_pyramid_zero(self, mock_stdout):
        inverted_pyramid(0)
        self.assertEqual(mock_stdout.getvalue(), "")

    @patch("sys.stdout", new_callable=StringIO)
    def test_inverted_pyramid_one(self, mock_stdout):
        inverted_pyramid(1)
        expected_output = "* \n"
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch("sys.stdout", new_callable=StringIO)
    def test_inverted_pyramid_negative(self, mock_stdout):
        inverted_pyramid(-5)
        self.assertEqual(mock_stdout.getvalue(), "")


class TestDiamond(unittest.TestCase):
    @patch("sys.stdout", new_callable=StringIO)
    def test_diamond_positive(self, mock_stdout):
        diamond(5)
        expected_output = "    * \n   * * \n  * * * \n * * * * \n* * * * * \n * * * * \n  * * * \n   * * \n    * \n"
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch("sys.stdout", new_callable=StringIO)
    def test_diamond_zero(self, mock_stdout):
        diamond(0)
        self.assertEqual(mock_stdout.getvalue(), "")

    @patch("sys.stdout", new_callable=StringIO)
    def test_diamond_one(self, mock_stdout):
        diamond(1)
        expected_output = "* \n"
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch("sys.stdout", new_callable=StringIO)
    def test_diamond_negative(self, mock_stdout):
        diamond(-5)
        self.assertEqual(mock_stdout.getvalue(), "")


class TestDiamondFilled(unittest.TestCase):
    @patch("sys.stdout", new_callable=StringIO)
    def test_diamond_filled_positive(self, mock_stdout):
        diamond_filled(5)
        expected_output = (
            "    *\n"
            "   ***\n"
            "  *****\n"
            " *******\n"
            "*********\n"
            " *******\n"
            "  *****\n"
            "   ***\n"
            "    *\n"
        )
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch("sys.stdout", new_callable=StringIO)
    def test_diamond_filled_zero(self, mock_stdout):
        diamond_filled(0)
        self.assertEqual(mock_stdout.getvalue(), "")

    @patch("sys.stdout", new_callable=StringIO)
    def test_diamond_filled_one(self, mock_stdout):
        diamond_filled(1)
        expected_output = "*\n"
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch("sys.stdout", new_callable=StringIO)
    def test_diamond_filled_negative(self, mock_stdout):
        diamond_filled(-5)
        self.assertEqual(mock_stdout.getvalue(), "")


class TestHalfDiamond(unittest.TestCase):
    @patch("sys.stdout", new_callable=StringIO)
    def test_half_diamond_positive(self, mock_stdout):
        half_diamond(5)
        expected_output = (
            "* \n* * \n* * * \n* * * * \n* * * * * \n* * * * \n* * * \n* * \n* \n"
        )
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch("sys.stdout", new_callable=StringIO)
    def test_half_diamond_zero(self, mock_stdout):
        half_diamond(0)
        self.assertEqual(mock_stdout.getvalue(), "")

    @patch("sys.stdout", new_callable=StringIO)
    def test_half_diamond_one(self, mock_stdout):
        half_diamond(1)
        expected_output = "* \n"
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch("sys.stdout", new_callable=StringIO)
    def test_half_diamond_negative(self, mock_stdout):
        half_diamond(-5)
        self.assertEqual(mock_stdout.getvalue(), "")


class RightTriangleBinary(unittest.TestCase):
    @patch("sys.stdout", new_callable=StringIO)
    def test_right_triangle_binary_positive(self, mock_stdout):
        input_value = 5
        right_triangle_binary_1(input_value)
        output_1 = mock_stdout.getvalue()
        mock_stdout.truncate(0)
        mock_stdout.seek(0)
        right_triangle_binary_2(input_value)
        output_2 = mock_stdout.getvalue()
        expected_output = "1\n0 1\n1 0 1\n0 1 0 1\n1 0 1 0 1\n"
        self.assertEqual(output_1, output_2)
        # self.assertTrue(output_1 == output_2 == expected_output)

    @patch("sys.stdout", new_callable=StringIO)
    def test_right_triangle_binary_zero(self, mock_stdout):
        input_value = 0
        right_triangle_binary_1(input_value)
        output_1 = mock_stdout.getvalue()
        mock_stdout.truncate(0)
        mock_stdout.seek(0)
        right_triangle_binary_2(input_value)
        output_2 = mock_stdout.getvalue()
        self.assertTrue(output_1 == output_2 == "")

    @patch("sys.stdout", new_callable=StringIO)
    def test_right_triangle_binary_one(self, mock_stdout):
        input_value = 1
        right_triangle_binary_1(input_value)
        output_1 = mock_stdout.getvalue()
        mock_stdout.truncate(0)
        mock_stdout.seek(0)
        right_triangle_binary_2(input_value)
        output_2 = mock_stdout.getvalue()
        expected_output = "1\n"
        self.assertEqual(output_1, output_2)
        # self.assertTrue(output_1 == output_2 == expected_output)

    @patch("sys.stdout", new_callable=StringIO)
    def test_right_triangle_binary_negative(self, mock_stdout):
        input_value = -5
        right_triangle_binary_1(input_value)
        output_1 = mock_stdout.getvalue()
        mock_stdout.truncate(0)
        mock_stdout.seek(0)
        right_triangle_binary_2(input_value)
        output_2 = mock_stdout.getvalue()
        self.assertTrue(output_1 == output_2 == "")


if __name__ == "__main__":
    unittest.main()
