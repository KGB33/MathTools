from mttools.number_theory_tools import perfect_factors, gcd

import pytest


class TestPerfectFactors:
    @pytest.mark.parametrize("n,e", [(32, [1, 2, 4, 8, 16, 32]),])
    def test_valid_input(self, n, e):
        for factor in perfect_factors(n):
            assert factor in e
            e.remove(factor)
        assert not e  # Should be empty

    @pytest.mark.parametrize("n,e", [(36, [1, 2, 3, 4, 6, 9, 12, 18, 36]),])
    def test_perfect_square(self, n, e):
        for factor in perfect_factors(n):
            assert factor in e
            e.remove(factor)
        assert not e  # Should be empty


class TestGCD:
    @pytest.mark.parametrize(
        "a,b,e",
        [
            (1, 1, 1),
            (0, 0, 0),
            (-1, -1, 1),
            (0, 123456, 123456),
            (1, 123456, 1),
            (-1, -123456, 1),
            (7, 3, 1),
            (3, 7, 1),
            (150, 100, 50),
        ],
    )
    def test_gcd(self, a, b, e):
        assert e == gcd(a, b)
