from hypothesis import given
import hypothesis.strategies as st
from pytest import raises

from mttools.geometry_tools import (
    distance,
    area_of_circle,
    rect_bar,
    round_bar,
    Tbeam,
    Ibeam_equal_flange,
    Ibeam_unequal_flange,
)


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


class TestRectBar:
    def test_rect_bar(self):
        assert rect_bar(3, 0.5) == {
            "Centroid": (0.25, 1.5),
            "Area": 1.5,
            "Ixx": 1.125,
            "Iyy": 0.03125,
            "Sx": 0.75,
            "Sy": 0.125,
        }

    def test_zero_rect_bar(self):
        with raises(ValueError):
            rect_bar(1, 0)


class TestRoundBar:
    def test_hollow_bar(self):
        assert round_bar(18, 15) == {
            "Centroid": 9.0,
            "Area": 77.75441817634739,
            "Ixx": 2667.9484736759196,
            "Sxx": 296.4387192973244,
        }

    def test_solid_bar_one(self):
        assert round_bar(13, 0) == {
            "Centroid": 6.5,
            "Area": 132.73228961416876,
            "Ixx": 1401.9848090496575,
            "Sxx": 215.68997062302424,
        }

    def test_solid_bar_two(self):
        assert round_bar(8) == {
            "Centroid": 4.0,
            "Area": 50.26548245743669,
            "Ixx": 201.06192982974676,
            "Sxx": 50.26548245743669,
        }

    def test_no_outside(self):
        with raises(ValueError):
            round_bar(-3)

    def test_negative_inside(self):
        with raises(ValueError):
            round_bar(5, -2)


class TestTbeam:
    def test_Tbeam(self):
        assert Tbeam(4, 0.5, 4, 0.5) == {
            "Centroid": (2.0, 2.8166666666666664),
            "Area": 3.75,
            "Ixx": 5.5614583333333325,
            "Iyy": 2.703125,
            "Sx": 1.9744822485207099,
            "Sy": 1.3515625,
        }

    def test_zero_Tbeam(self):
        with raises(ValueError):
            Tbeam(4, 0.5, 10, -1)


class TestIbeam_equal_flange:
    def test_Ibeam_equal_flange(self):
        assert Ibeam_equal_flange(8, 0.5, 6, 0.75) == {
            "Centroid": (3.0, 4.0),
            "Area": 12.25,
            "Ixx": 130.13020833333334,
            "Iyy": 27.067708333333332,
            "Sx": 32.532552083333336,
            "Sy": 9.022569444444445,
        }

    def test_zero_Ibeam_equal_flange(self):
        with raises(ValueError):
            Ibeam_equal_flange(-1, 1, 3, 0.25)


class TestIbeam_unequal_flange:
    def test_Ibeam_unequal_flange(self):
        assert Ibeam_unequal_flange(8, 0.5, (9, 0.75), (6, 1)) == {
            "Centroid": (4.5, 4.243110236220472),
            "Area": 15.875,
            "Ixx": 172.29872559875326,
            "Iyy": 63.627604166666664,
            "Sx": 40.60670498917498,
            "Sy": 14.139467592592592,
        }

    def test_negative_Ibeam_unequal_flange(self):
        with raises(ValueError):
            Ibeam_unequal_flange(6, 2, (0, 0.5), (-4, 1))
