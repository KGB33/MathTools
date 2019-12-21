from mttools.GeometryTools import distance


class TestDistance:
    def test_one_dimensional_input(self):
        assert 5 == distance([0], [5])

    def test_really_big_dimensional_input(self):
        assert 500 == distance(
            [0 for _ in range(0, 10000)], [5 for _ in range(0, 10000)]
        )

    def test_negative_coords(self):
        assert 500 == distance(
            [0 for _ in range(0, 10000)], [-5 for _ in range(0, 10000)]
        )
