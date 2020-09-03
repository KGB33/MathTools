from hypothesis import given
import hypothesis.strategies as st
from pytest import raises

from mttools.geometry_tools import distance, area_of_circle


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


class TestAreaOfCircle:
    def test_interger_radius(self):
        assert area_of_circle(3) == 28.274333882308138

    @given(st.floats(allow_nan=False, allow_infinity=False))
    def test_inverse_radius_gives_same_area(self, radius):
        inverse_radius = radius * -1
        assert area_of_circle(radius) == area_of_circle(inverse_radius)

    @given(st.complex_numbers(allow_nan=False, allow_infinity=False))
    def test_inverse_complex_radius(self, radius):
        inverse_radius = radius * -1
        assert area_of_circle(radius) == area_of_circle(inverse_radius)
