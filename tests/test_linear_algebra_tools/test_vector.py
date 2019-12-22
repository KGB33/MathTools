import pytest

from mttools.LinearAlgebraTools import Vector


@pytest.fixture
def v():
    return Vector([1, 2, 3])


class TestInit:
    def test_valid(self):
        v = Vector([1, 2, 3])
        assert v.coords == (1, 2, 3)
        assert v.dimension == 3

    def test_empty_coords(self):
        with pytest.raises(ValueError) as excinfo:
            v = Vector([])

        assert "Coords must not be empty." == str(excinfo.value)

    def test_uniterable_coords(self):
        with pytest.raises(TypeError) as excinfo:
            v = Vector(123)

        assert "Coords must be a list or tuple." == str(excinfo.value)

    def test_str_coords(self):
        with pytest.raises(TypeError) as excinfo:
            v = Vector("123")

        assert "Coords must be a list or tuple." == str(excinfo.value)


class TestStr:
    def test_str(self, v):
        assert v.__str__() == "Vector: [1, 2, 3]"


class TestEq:
    def test_equal(self):
        v = Vector([1, 2, 3])
        u = Vector([1, 2, 3])
        assert v == u

    def test_unequal(self):
        v = Vector([3, 2, 1])
        u = Vector([1, 2, 3])
        assert v != u
