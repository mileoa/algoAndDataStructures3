import unittest
import random
from typing import List

from QuickSort import QuickSort


class QuickSortTests(unittest.TestCase):

    def test_regression(self) -> None:
        array: List[int] = [5, 2, 9, 1, 3, 6, 7]
        QuickSort(array, 0, len(array) - 1)
        self.assertEqual(array, [1, 2, 3, 5, 6, 7, 9])

    def test_empty(self) -> None:
        empty_array: List[int] = []
        QuickSort(empty_array, 0, len(empty_array) - 1)
        self.assertEqual(empty_array, [])

    def test_random(self) -> None:
        for repeat in range(1000):
            array: List[int] = list(range(random.randint(0, 100)))
            array_native_sorted: List[int] = array.copy()
            random.shuffle(array)
            QuickSort(array, 0, len(array) - 1)
            self.assertEqual(array, array_native_sorted)

    def test_border(self) -> None:
        array: List[int] = [1]
        QuickSort(array, 0, len(array) - 1)
        self.assertEqual(array, [1])


if __name__ == "__main__":
    unittest.main()
