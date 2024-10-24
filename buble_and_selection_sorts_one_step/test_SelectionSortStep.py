import unittest
import random
from typing import List

from buble_and_selection_sorts_one_step import SelectionSortStep


class SelectionSortStepTests(unittest.TestCase):

    def test_regression(self):
        first_sorted_list: List[int] = [4, 3, 1, 2]
        for i in range(len(first_sorted_list)):
            SelectionSortStep(first_sorted_list, i)
            if i == 0:
                self.assertEqual(first_sorted_list, [1, 3, 4, 2])
            elif i == 1:
                self.assertEqual(first_sorted_list, [1, 2, 4, 3])
            elif i == 2:
                self.assertEqual(first_sorted_list, [1, 2, 3, 4])
            elif i == 3:
                self.assertEqual(first_sorted_list, [1, 2, 3, 4])

        second_sorted_list: List[int] = [4, 3, 1, 2, 3, 2, 1, 5, 4, 3]
        second_native_sorted_list: List = second_sorted_list.copy()
        second_native_sorted_list.sort()
        for i in range(len(second_sorted_list)):
            SelectionSortStep(second_sorted_list, i)
        self.assertEqual(second_sorted_list, second_native_sorted_list)

    def test_border(self):
        sorted_list: List[int] = [1]
        SelectionSortStep(sorted_list, 0)
        self.assertEqual(sorted_list, [1])


if __name__ == "__main__":
    unittest.main()
