from mttools.NumberTheoryTools import perfect_factors, gcd, lcf


def pytest_generate_tests(metafunc):
    # called once per each test function
    funcarglist = metafunc.cls.params[metafunc.function.__name__]
    argnames = sorted(funcarglist[0])
    metafunc.parametrize(
        argnames, [[funcargs[name] for name in argnames] for funcargs in funcarglist]
    )


class TestPerfectFactors:
    params = {
        "test_valid_input": {"n": 32, "e": [1, 2, 4, 8, 16, 32]},
        "test_perfect_square": {"n": 36, "e": [1, 2, 3, 4, 6, 9, 12, 18, 36]},
    }

    def test_valid_input(self, n, e):
        for factor in perfect_factors(n):
            assert factor in e
            e.remove(factor)
        assert not e  # Should be empty

    def test_perfect_square(self, n, e):
        for factor in perfect_factors(n):
            assert factor in e
            e.remove(factor)
        assert not e  # Should be empty


class TestGCD:
    params = {
        "test_gcd": [
            {"a": 1, "b": 1, "e": 1},
            {"a": 0, "b": 0, "e": 0},
            {"a": -1, "b": -1, "e": 1},
            {"a": 0, "b": 123456, "e": 123456},
            {"a": 1, "b": 123456, "e": 123456},
            {"a": -1, "b": -123456, "e": 1},
            {"a": 7, "b": 3, "e": 1},
            {"a": 3, "b": 7, "e": 1},
            {"a": 150, "b": 100, "e": 50},
        ]
    }

    def test_gcd(self, a, b, e):
        assert e == gcd(a, b)


class TestLCM:
    params = {"test_lcm": {}}

    def test_lcm(a, b):
        pass
