import unittest
import random

from KnuthSequence import KnuthSequence


class KnuthSequenceTests(unittest.TestCase):

    def test_regression(self):
        self.assertEqual(KnuthSequence(15), [13, 4, 1])
        self.assertEqual(KnuthSequence(15), [13, 4, 1])
        self.assertEqual(KnuthSequence(0), [1])
        self.assertEqual(KnuthSequence(1), [1])
        self.assertEqual(KnuthSequence(2), [1])
        self.assertEqual(KnuthSequence(5), [4, 1])
        self.assertEqual(KnuthSequence(13), [13, 4, 1])
        self.assertEqual(KnuthSequence(365), [364, 121, 40, 13, 4, 1])


if __name__ == "__main__":
    unittest.main()
