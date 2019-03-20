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


class TestSqrt(unittest.TestCase):
    # Expected floats from WolframAlpha

    def test_pos_int(self):
        sol = sqrt(100)
        self.assertEqual(10, sol)

    def test_pos_float(self):
        sol = sqrt(50.599)
        expected = 7.113297406969569411748839730419181694884373115168164007497
        self.assertAlmostEqual(expected, sol)

    def test_pos_num_less_than_one(self):
        sol = sqrt(0.50)
        expected = 0.707106781186547524400844362104849039284835937688474036588
        self.assertAlmostEqual(expected, sol)

    def test_zero(self):
        sol = sqrt(0)
        self.assertEqual(0, sol)
        
    def test_neg_int(self):
        sol = sqrt(-100)
        self.assertEqual(10j, sol)

    def test_neg_float(self):
        sol = sqrt(-50.599)
        expected = 7.113297406969569411748839730419181694884373115168164007497j
        self.assertAlmostEqual(expected, sol)

    def test_neg_num_less_than_one(self):
        sol = sqrt(-0.50)
        expected = 0.707106781186547524400844362104849039284835937688474036588j
        self.assertAlmostEqual(expected, sol)


if __name__ == '__main__':
    unittest.main()
