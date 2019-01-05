import unittest
from NumberTools import *


class TestPerfectFactors(unittest.TestCase):

    def test_valid_input(self):
        expected = [1, 2, 4, 8, 16, 32]
        for factor in perfect_factors(32):
            self.assertIn(factor, expected)
            expected.remove(factor)
        self.assertFalse(expected)  # Should be empty

    def test_perfect_square(self):
        expected = [1, 2, 3, 4, 6, 9, 12, 18, 36]
        for factor in perfect_factors(36):
            self.assertIn(factor, expected)
            expected.remove(factor)
        self.assertFalse(expected) # Should be empty


if __name__ == '__main__':
    unittest.main()
