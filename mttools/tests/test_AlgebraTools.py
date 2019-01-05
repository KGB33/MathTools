import unittest
from AlgebraTools import *


class TestQuadraticFormula(unittest.TestCase):

    def test_2_real_sol(self):
        sol = quadratic_formula(5, 6, 1)
        expt = (-0.2, -1)
        self.assertEqual(expt, sol)

    def test_1_real_sol(self):
        sol = quadratic_formula(1, -8, 16)
        expt = (4,)
        self.assertEqual(expt, sol)

    def test_2_complex_sol(self):
        sol = quadratic_formula(5, 2, 1)
        expt = (-0.2 + 0.4j, -0.2 - 0.4j)
        self.assertEqual(expt, sol)


if __name__ == '__main__':
    unittest.main()
