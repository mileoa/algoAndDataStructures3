import unittest
import random
from typing import List

from InsertionSortStep import InsertionSortStep


class InsertionSortStepTests(unittest.TestCase):

    def test_regression(self) -> None:
        array: List[int] = [7, 6, 5, 4, 3, 2, 1]
        InsertionSortStep(array, 3, 0)
        self.assertEqual(array, [1, 6, 5, 4, 3, 2, 7])
        InsertionSortStep(array, 3, 1)
        self.assertEqual(array, [1, 3, 5, 4, 6, 2, 7])
        InsertionSortStep(array, 3, 2)
        self.assertEqual(array, [1, 3, 2, 4, 6, 5, 7])
        InsertionSortStep(array, 3, 3)
        self.assertEqual(array, [1, 3, 2, 4, 6, 5, 7])

        second_array: List[int] = [1, 6, 5, 4, 3, 2, 7]
        InsertionSortStep(second_array, 3, 1)
        self.assertEqual(second_array, [1, 3, 5, 4, 6, 2, 7])

    def test_border(self) -> None:
        array: List[int] = [7]
        InsertionSortStep(array, 1, 0)
        self.assertEqual(array, [7])

    def test_random(self) -> None:
        for i in range(10000):
            array: List[int] = [
                random.randint(0, 10) for dummy in range(random.randint(1, 100))
            ]
            array_native_sorted: List[int] = array.copy()
            array_native_sorted.sort()
            InsertionSortStep(array, 1, 0)
            self.assertEqual(array, array_native_sorted)


if __name__ == "__main__":
    unittest.main()
