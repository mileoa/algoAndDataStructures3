import unittest
import random
from typing import List

from ArrayChunk import ArrayChunk


class ArrayChunkTests(unittest.TestCase):

    def test_regression(self) -> None:
        first_array: List[int] = [7, 5, 6, 4, 3, 1, 2]
        self.assertEqual(ArrayChunk(first_array), 3)
        self.assertEqual(first_array, [2, 1, 3, 4, 6, 5, 7])

        second_array: List[int] = [7, 5, 6, 8, 4, 3, 1, 2]
        self.assertEqual(ArrayChunk(second_array), 7)
        self.assertEqual(second_array, [2, 1, 3, 4, 7, 6, 5, 8])

        third_array: List[int] = [1, 5, 3, 4, 6, 8, 7, 9]
        self.assertEqual(ArrayChunk(third_array), 4)
        self.assertEqual(third_array, [1, 5, 3, 4, 6, 8, 7, 9])

    def test_border(self) -> None:
        first_array: List[int] = [7, 5, 6, 4, 8, 3, 1, 2]
        self.assertEqual(ArrayChunk(first_array), 7)
        self.assertEqual(first_array, [7, 5, 6, 4, 2, 3, 1, 8])

        second_array: List[int] = [7, 5, 6, 4, 1, 3, 8, 2]
        self.assertEqual(ArrayChunk(second_array), 0)
        self.assertEqual(second_array, [1, 5, 6, 4, 7, 3, 8, 2])


if __name__ == "__main__":
    unittest.main()
