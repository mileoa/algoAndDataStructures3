import unittest
import random
from typing import List

from ksort import ksort


class KSORTTests(unittest.TestCase):

    def test_regression_index(self):
        k = ksort()
        self.assertEqual(k.index("a00"), 0)
        self.assertEqual(k.index("b13"), 113)
        self.assertEqual(k.index("h99"), 799)
        self.assertEqual(k.index("a000"), -1)
        self.assertEqual(k.index("aa00"), -1)
        self.assertEqual(k.index("aa0"), -1)
        self.assertEqual(k.index("z00"), -1)

    def test_regression_add(self):
        k = ksort()
        self.assertTrue(k.add("a00"))
        self.assertTrue(k.add("b13"))
        self.assertTrue(k.add("h99"))
        self.assertFalse(k.add("a000"))
        self.assertFalse(k.add("aa00"))
        self.assertFalse(k.add("aa0"))
        self.assertFalse(k.add("z00"))
        for i, el in enumerate(k.items):
            if i == 0:
                self.assertEqual(el, "a00")
                continue
            if i == 113:
                self.assertEqual(el, "b13")
                continue
            if i == 799:
                self.assertEqual(el, "h99")
                continue
            self.assertIsNone(el)


if __name__ == "__main__":
    unittest.main()
