import pytest

from mttools.number_theory_tools.Primes import (
    division_primality_test,
    fermat_primality_test,
    largest_prime_less_than,
    prime_factors,
    sieve_of_eratosthenes,
    lucas_lehmer_primality_test,
)


class TestFermatPrimalityTest:
    def test_carmichael_nums(self):
        assert not fermat_primality_test(561, 3)
        assert not fermat_primality_test(410041, 3)
        assert not fermat_primality_test(512461, 3)

    def test_with_prime(self):
        assert fermat_primality_test(3, 3)
        assert fermat_primality_test(277, 3)
        assert fermat_primality_test(105607, 3)

    def test_with_composite(self):
        assert not fermat_primality_test(10000, 3)
        assert not fermat_primality_test(-1, 3)
        assert not fermat_primality_test(6530, 3)


class TestDivisionPrimalityTest:
    def test_with_prime(self):
        assert division_primality_test(3)
        assert division_primality_test(277)
        assert division_primality_test(105607)

    def test_with_composite(self):
        assert not division_primality_test(10000)
        assert not division_primality_test(-1)
        assert not division_primality_test(6530)


class TestSieveOfEratosthenes:
    def test_valid_upper_bound(self):
        expected = [2, 3, 5, 7, 11, 13, 17, 19]
        assert expected == sieve_of_eratosthenes(20)


class TestPrimeFactors:
    def test_large_number(self):
        large_composite = pow(2 * 3 * 5 * 7, 5)
        expected = {2: 5, 3: 5, 5: 5, 7: 5}
        assert expected == prime_factors(large_composite)

    def test_small_number(self):
        expected = {2: 5}
        assert expected == prime_factors(32)

    def test_prime_number(self):
        assert {23: 1} == prime_factors(23)


class TestLargestPrimeLessThan:
    def test_no_primes_less_than(self):
        assert largest_prime_less_than(2) is None

    def test_primes_less_than_3(self):
        assert 2 == largest_prime_less_than(3)

    def test_primes_less_than_large_num(self):
        assert 105023 == largest_prime_less_than(105030)


class TestLucasLehmerPrimalityTest:
    def test_requires_mersenne_number(self):
        with pytest.raises(ValueError):
            lucas_lehmer_primality_test(25)

    def test_with_prime(self):
        assert lucas_lehmer_primality_test(2 ** 31 - 1)

    def test_with_composite(self):
        assert not lucas_lehmer_primality_test(2 ** 30 - 1)
