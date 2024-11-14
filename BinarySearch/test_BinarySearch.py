import unittest
import random

from BinarySearch import BinarySearch


class BinarySearchTests(unittest.TestCase):

    def test_regression_Step_and_GetResult(self):
        bs_one = BinarySearch([1, 2, 3, 4, 5, 6, 7, 8, 9])
        bs_one.Step(3)
        self.assertEqual(bs_one.Left, 0)
        self.assertEqual(bs_one.Right, 3)
        self.assertEqual(bs_one.GetResult(), "0")

        bs_one.Step(3)
        self.assertEqual(bs_one.Left, 2)
        self.assertEqual(bs_one.Right, 3)
        self.assertEqual(bs_one.GetResult(), "+1")

        bs_one.Step(3)
        self.assertEqual(bs_one.Left, 2)
        self.assertEqual(bs_one.Right, 3)
        self.assertEqual(bs_one.GetResult(), "+1")

        bs_one.Step(3)
        self.assertEqual(bs_one.Left, 2)
        self.assertEqual(bs_one.Right, 3)
        self.assertEqual(bs_one.GetResult(), "+1")

        bs_two = BinarySearch([1, 2, 3, 4, 5, 6, 7, 8, 9])
        bs_two.Step(10)
        self.assertEqual(bs_two.Left, 5)
        self.assertEqual(bs_two.Right, 8)
        self.assertEqual(bs_two.GetResult(), "0")

        bs_two.Step(10)
        self.assertEqual(bs_two.Left, 7)
        self.assertEqual(bs_two.Right, 8)
        self.assertEqual(bs_two.GetResult(), "-1")

        bs_two.Step(10)
        self.assertEqual(bs_two.Left, 7)
        self.assertEqual(bs_two.Right, 8)
        self.assertEqual(bs_two.GetResult(), "-1")

        bs_three = BinarySearch([1, 2, 3, 4, 5, 6, 7, 8, 9])
        bs_three.Step(9)
        self.assertEqual(bs_three.Left, 5)
        self.assertEqual(bs_three.Right, 8)
        self.assertEqual(bs_three.GetResult(), "0")

        bs_three.Step(9)
        self.assertEqual(bs_three.Left, 7)
        self.assertEqual(bs_three.Right, 8)
        self.assertEqual(bs_three.GetResult(), "+1")

        bs_three.Step(9)
        self.assertEqual(bs_three.Left, 7)
        self.assertEqual(bs_three.Right, 8)
        self.assertEqual(bs_three.GetResult(), "+1")


if __name__ == "__main__":
    unittest.main()
