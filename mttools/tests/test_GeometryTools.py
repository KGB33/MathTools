import unittest
from GeometryTools import *


class TestDistance(unittest.TestCase):

    def test_one_dimensional_input(self):
        self.assertEqual(5, distance([0], [5]))

    def test_really_big_dimensional_input(self):
        self.assertEqual(500, distance([0 for _ in range(0, 10000)], [5 for _ in range(0, 10000)]))

    def test_negative_coords(self):
        self.assertEqual(500, distance([0 for _ in range(0, 10000)], [-5 for _ in range(0, 10000)]))


if __name__ == '__main__':
    unittest.main()
