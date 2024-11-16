import unittest
import random

from GallopingSearch import BinarySearch


class GallopingSearchTests(unittest.TestCase):

    def test_regression_GallopingSearch(self):
        b = BinarySearch(list(range(100)))
        self.assertTrue(b.GallopingSearch(list(range(100)), 5))
        self.assertTrue(b.GallopingSearch(list(range(100)), 6))
        self.assertTrue(b.GallopingSearch(list(range(100)), 3))
        self.assertTrue(b.GallopingSearch(list(range(100)), 0))
        self.assertTrue(b.GallopingSearch(list(range(100)), 99))
        self.assertFalse(b.GallopingSearch(list(range(100)), -1))
        self.assertFalse(b.GallopingSearch(list(range(100)), 100))


if __name__ == "__main__":
    unittest.main()
