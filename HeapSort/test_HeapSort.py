import unittest
import random
from typing import List

from HeapSort import HeapSort


class HeapSortTests(unittest.TestCase):

    def test_regression(self):
        array: List[int] = [5, 3, 2, 1, 5, 6]
        heap_sort: HeapSort = HeapSort(array)
        self.assertEqual(heap_sort.GetNextMax(), 6)
        self.assertEqual(heap_sort.GetNextMax(), 5)
        self.assertEqual(heap_sort.GetNextMax(), 5)
        self.assertEqual(heap_sort.GetNextMax(), 3)
        self.assertEqual(heap_sort.GetNextMax(), 2)
        self.assertEqual(heap_sort.GetNextMax(), 1)
        self.assertEqual(heap_sort.GetNextMax(), -1)
        self.assertEqual(heap_sort.GetNextMax(), -1)

    def test_empty(self):
        heap_sort: HeapSort = HeapSort([])
        self.assertEqual(heap_sort.GetNextMax(), -1)

    def test_random(self):
        for repeat in range(1000):
            array: List[int] = [
                random.randint(0, 10) for i in range(random.randint(0, 100))
            ]
            heap_sort: HeapSort = HeapSort(array)
            array_native_sorted: List = array.copy()
            array_native_sorted.sort()
            while len(array_native_sorted) != 0:
                self.assertEqual(heap_sort.GetNextMax(), array_native_sorted.pop())
            self.assertEqual(heap_sort.GetNextMax(), -1)


if __name__ == "__main__":
    unittest.main()
