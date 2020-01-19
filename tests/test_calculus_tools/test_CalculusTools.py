from math import isinf

from pytest import approx

from mttools.CalculusTools import limit


class TestLimit:
    def test_func(self):
        f = lambda x: x * x
<<<<<<< HEAD:mttools/tests/test_CalculusTools.py
        assert 0 == approx(limit(f, 0))
=======
        assert approx(limit(f, 0), 0, abs=10 ** -10)
>>>>>>> 297b4d580abd0579d79eec89d3751a18f74d2b54:tests/test_calculus_tools/test_CalculusTools.py
        assert 4 == approx(limit(f, 2))
        assert 4 == approx(limit(f, -2))

    def test_hole(self):
        f = lambda x: ((x + 3) * (x - 2)) / ((x + 3) * (x + 2))
        assert 5 == approx(limit(f, -3))

    def test_vertical_asymptote_no_limit(self):
        f = lambda x: ((x + 3) * (x - 2)) / ((x + 3) * (x + 2))
        assert limit(f, -2) is None

    def test_vertical_asymptote_has_limit(self):
        f = lambda x: 1 / (x * x)
        assert isinf(limit(f, 0))
        assert limit(f, 0) > 0

    def test_vertical_asymptote_has_neg_limit(self):
        f = lambda x: -1 / (x * x)
        assert limit(f, 0) < 0
