import unittest
import random
from typing import List

from MergeSort import MergeSort


class MergeSortTests(unittest.TestCase):

    def test_regression(self):
        first_array: List[int] = [5, 3, 2, 1, 5, 6]
        self.assertEqual(MergeSort(first_array), [1, 2, 3, 5, 5, 6])

        second_array: List[int] = [5, 3, 2, 1, 6]
        self.assertEqual(MergeSort(second_array), [1, 2, 3, 5, 6])

    def test_border(self):
        empty_array: List[int] = [1]
        self.assertEqual(MergeSort(empty_array), [1])

    def test_random(self):
        for repeat in range(1000):
            array: List[int] = [
                random.randint(0, 10) for i in range(random.randint(1, 100))
            ]
            array_native_sorted: List = array.copy()
            array_native_sorted.sort()
            self.assertEqual(MergeSort(array), array_native_sorted)


if __name__ == "__main__":
    unittest.main()
