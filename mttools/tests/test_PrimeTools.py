import unittest
from PrimeTools import *


class TestFermatPrimalityTest(unittest.TestCase):

    def test_carmichael_nums(self):
        self.assertFalse(fermat_primality_test(561, 3))
        self.assertFalse(fermat_primality_test(410041, 3))
        self.assertFalse(fermat_primality_test(512461, 3))

    def test_with_prime(self):
        self.assertTrue(fermat_primality_test(3, 3))
        self.assertTrue(fermat_primality_test(277, 3))
        self.assertTrue(fermat_primality_test(105607, 3))

    def test_with_composite(self):
        self.assertFalse(fermat_primality_test(10000, 3))
        self.assertFalse(fermat_primality_test(-1, 3))
        self.assertFalse(fermat_primality_test(6530, 3))


class TestDivisionPrimalityTest(unittest.TestCase):
    
    def test_with_prime(self):
        self.assertTrue(division_primality_test(3))
        self.assertTrue(division_primality_test(277))
        self.assertTrue(division_primality_test(105607))

    def test_with_composite(self):
        self.assertFalse(division_primality_test(10000))
        self.assertFalse(division_primality_test(-1))
        self.assertFalse(division_primality_test(6530))


class TestSieveOfEratosthenes(unittest.TestCase):

    def test_valid_upper_bound(self):
        expected = {2, 3, 5, 7, 11, 13, 17, 19}
        self.assertEqual(expected, sieve_of_eratosthenes(20))


class TestPrimeFactors(unittest.TestCase):

    def test_large_number(self):
        large_composite = pow(2*3*5*7, 5)
        expected = {2: 5, 3: 5, 5: 5, 7: 5,}
        self.assertEqual(expected, prime_factors(large_composite))

    def test_small_number(self):
        expected = {2: 5}
        self.assertEqual(expected, prime_factors(32))

    def test_prime_number(self):
        self.assertEqual({23: 1}, prime_factors(23))


class TestLargestPrimeLessThan(unittest.TestCase):

    def test_no_primes_less_than(self):
        self.assertIsNone(largest_prime_less_than(2))

    def test_primes_less_than_3(self):
        self.assertEqual(2, largest_prime_less_than(3))

    def test_primes_less_than_large_num(self):
        self.assertEqual(105023, largest_prime_less_than(105030))


if __name__ == '__main__':
    unittest.main()
