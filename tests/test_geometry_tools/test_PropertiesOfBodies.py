from pytest import raises


from mttools.geometry_tools.PropertiesOfBodies import (
    rect_bar,
    round_bar,
    Tbeam,
    Ibeam_equal_flange,
    Ibeam_unequal_flange,
)


class TestRectBar:
    def test_rect_bar(self):
        assert rect_bar(3, 0.5) == {
            "Centroid X": 0.25,
            "Centroid Y": 1.5,
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
            "Centroid X": 2.0,
            "Centroid Y": 2.8166666666666664,
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
            "Centroid X": 3.0,
            "Centroid Y": 4.0,
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
            "Centroid X": 4.5,
            "Centroid Y": 4.243110236220472,
            "Area": 15.875,
            "Ixx": 172.29872559875326,
            "Iyy": 63.627604166666664,
            "Sx": 40.60670498917498,
            "Sy": 14.139467592592592,
        }

    def test_negative_Ibeam_unequal_flange(self):
        with raises(ValueError):
            Ibeam_unequal_flange(6, 2, (0, 0.5), (-4, 1))
