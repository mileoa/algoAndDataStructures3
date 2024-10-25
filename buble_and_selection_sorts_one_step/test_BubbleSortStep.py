import unittest
import random
from typing import List
from buble_and_selection_sorts_one_step import BubbleSortStep


class BubbleSortStepTests(unittest.TestCase):

    def test_regression(self):
        array: List[int] = [4, 5, 2, 1, 0]
        self.assertFalse(BubbleSortStep(array))
        self.assertEqual(array, [4, 2, 1, 0, 5])
        self.assertFalse(BubbleSortStep(array))
        self.assertEqual(array, [2, 1, 0, 4, 5])
        self.assertFalse(BubbleSortStep(array))
        self.assertEqual(array, [1, 0, 2, 4, 5])
        self.assertFalse(BubbleSortStep(array))
        self.assertEqual(array, [0, 1, 2, 4, 5])
        self.assertTrue(BubbleSortStep(array))
        self.assertEqual(array, [0, 1, 2, 4, 5])

        array: List = [4, 3, 1, 2]
        self.assertFalse(BubbleSortStep(array))
        self.assertEqual(array, [3, 1, 2, 4])
        self.assertFalse(BubbleSortStep(array))
        self.assertEqual(array, [1, 2, 3, 4])
        self.assertTrue(BubbleSortStep(array))
        self.assertEqual(array, [1, 2, 3, 4])

    def test_empty(self):
        empty_array: List[int] = []
        self.assertTrue(BubbleSortStep(empty_array))

    def test_border(self):
        array: List[int] = [4]
        self.assertTrue(BubbleSortStep(array))
        self.assertEqual(array, [4])


if __name__ == "__main__":
    unittest.main()
