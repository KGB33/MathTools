import unittest
from CalculusTools import *
from math import isinf


class TestLimit(unittest.TestCase):

    def test_func(self):
        f = lambda x: x * x
        self.assertAlmostEqual(0, limit(f, 0))
        self.assertAlmostEqual(4, limit(f, 2))
        self.assertAlmostEqual(4, limit(f, -2))

    def test_hole(self):
        f = lambda x: ((x + 3)*(x - 2))/((x + 3)*(x + 2))
        self.assertAlmostEqual(5, limit(f, -3))

    def test_vertical_asymptote_no_limit(self):
        f = lambda x: ((x + 3)*(x - 2)) / ((x + 3)*(x + 2))
        self.assertIsNone(limit(f, -2))

    def test_vertical_asymptote_has_limit(self):
        f = lambda x: 1 / (x * x)
        self.assertTrue(isinf(limit(f, 0)))
        self.assertTrue(limit(f, 0) > 0)

    def test_vertical_asymptote_has_neg_limit(self):
        f = lambda x: -1 / (x * x)
        self.assertTrue(isinf(limit(f, 0)))
        self.assertTrue(limit(f, 0) < 0)
