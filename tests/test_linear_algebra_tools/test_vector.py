import pytest

from mttools.LinearAlgebraTools import Vector
from mttools.Exceptions import DimensionError


@pytest.fixture
def v1():
    return Vector([1, 2, 3])


@pytest.fixture
def v2():
    return Vector([-1, 0.50, 10])


@pytest.fixture
def not_vectors():
    return [
        "string",
        ["list", 123, True],
        ("Tuple", 123, False),
        {"set", 123, None},
        {"Dict": 123},
    ]


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
    def test_str(self, v1):
        assert v1.__str__() == "Vector: [1, 2, 3]"


class TestEq:
    def test_equal(self):
        v = Vector([1, 2, 3])
        u = Vector([1, 2, 3])
        assert v == u

    def test_unequal(self):
        v = Vector([3, 2, 1])
        u = Vector([1, 2, 3])
        assert v != u


class TestAdd:
    def test_valid(self, v1, v2):
        assert (2, 4, 6) == (v1 + v1).coords
        assert (0, 2.5, 13) == (v1 + v2).coords
        assert (-2, 1.0, 20) == (v2 + v2).coords

    def test_not_vector(self, v1, not_vectors):
        for value in not_vectors:
            with pytest.raises(TypeError) as excinfo:
                new_v = v1 + value
            assert f"Expected Type 'Vector', got type '{type(value)}'." == str(
                excinfo.value
            )

    def test_diff_dim(self, v1):
        u = Vector([1, 2, 3, 4])
        with pytest.raises(DimensionError) as excinfo:
            new_v = v1 + u
        assert (
            f"Cannot add Vector with self.dimension=3 to Vector with other.dimension=4."
            == str(excinfo.value)
        )


class TestSub:
    def test_valid(self, v1, v2):
        assert (0, 0, 0) == (v1 - v1).coords
        assert (2, 1.5, -7) == (v1 - v2).coords
        assert (0, 0.0, 0) == (v2 - v2).coords

    def test_not_vector(self, v1, not_vectors):
        for value in not_vectors:
            with pytest.raises(TypeError) as excinfo:
                new_v = v1 - value
            assert f"Expected Type 'Vector', got type '{type(value)}'." == str(
                excinfo.value
            )

    def test_diff_dim(self, v1):
        u = Vector([1, 2, 3, 4])
        with pytest.raises(DimensionError) as excinfo:
            new_v = v1 - u
        assert (
            f"Cannot add Vector with self.dimension=3 to Vector with other.dimension=4."
            == str(excinfo.value)
        )


class TestScalarMul:
    def test_valid(self, v1):
        new_v = v1 * 3
        assert (3, 6, 9) == new_v.coords

    def test_invalid(self, v1, not_vectors):
        for value in not_vectors:
            with pytest.raises(TypeError) as excinfo:
                new_v = v1 * value
            assert (
                f"Expected Type 'Vector' or 'numbers.real', got type '{type(value)}'."
                == str(excinfo.value)
            )


class TestVectorMul:
    def test_not_implemented(self, v1, v2):
        with pytest.raises(NotImplementedError) as excinfo:
            v1 * v2
        assert "NotImplementedError" in str(excinfo)


class TestMagnitude:
    def test_magnitude(self, v1, v2):
        assert 3.7416573867739413 == pytest.approx(v1.magnitude)
        assert 10.062305898749054 == pytest.approx(v2.magnitude)


class TestDirection:
    def test_direction(self, v1, v2):
        for a, b in zip(
            [0.2672612419124244, 0.5345224838248488, 0.8017837257372732], v1.direction
        ):
            assert a == pytest.approx(b)
        for a, b in zip(
            [-0.09938079899999065, 0.049690399499995326, 0.9938079899999065],
            v2.direction,
        ):
            assert a == pytest.approx(b)

    def test_zero_vector(self):
        v = Vector([0, 0, 0])
        with pytest.raises(ZeroDivisionError) as excinfo:
            u = v.direction
        assert f"Cannot normalize the zero vector." in str(excinfo.value)
