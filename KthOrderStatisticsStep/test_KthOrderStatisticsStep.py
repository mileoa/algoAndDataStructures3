import unittest
import random
from typing import List

from KthOrderStatisticsStep import KthOrderStatisticsStep


class KthOrderStatisticsStepTests(unittest.TestCase):

    def test_regression(self):
        array: List[int] = [3, 5, 2, 4, 1]
        self.assertEqual(KthOrderStatisticsStep(array, 0, len(array) - 1, 0), [0, 3])

        array: List[int] = [3, 5, 2, 4, 1]
        self.assertEqual(KthOrderStatisticsStep(array, 0, len(array) - 1, 4), [0, 4])

        array: List[int] = [3, 5, 2, 4, 1]
        self.assertEqual(KthOrderStatisticsStep(array, 0, len(array) - 1, 2), [0, 3])

    def test_border(self):
        array: List[int] = [3]
        self.assertEqual(KthOrderStatisticsStep(array, 0, len(array) - 1, 0), [0, 0])

        array: List[int] = [3, 5, 2, 4, 1]
        self.assertEqual(KthOrderStatisticsStep(array, 0, 0, 0), [0, 0])

        array: List[int] = [3, 5, 2, 4, 1]
        self.assertEqual(KthOrderStatisticsStep(array, 3, 3, 3), [3, 3])

        array: List[int] = [3, 5, 2, 4, 1]
        self.assertEqual(KthOrderStatisticsStep(array, 0, 0, 1), [1, 0])


if __name__ == "__main__":
    unittest.main()
