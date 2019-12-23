from mttools.NumberTheoryTools.NumberTools import perfect_factors


class TestPerfectFactors:
    def test_valid_input(self):
        expected = [1, 2, 4, 8, 16, 32]
        for factor in perfect_factors(32):
            assert factor in expected
            expected.remove(factor)
        assert not expected  # Should be empty

    def test_perfect_square(self):
        expected = [1, 2, 3, 4, 6, 9, 12, 18, 36]
        for factor in perfect_factors(36):
            assert factor in expected
            expected.remove(factor)
        assert not expected  # Should be empty
