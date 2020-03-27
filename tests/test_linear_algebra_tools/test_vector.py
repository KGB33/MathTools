import pytest

from math import pi

from mttools.LinearAlgebraTools.Vector import Vector
from mttools.utils.Exceptions import DimensionError


def test_tox():
    assert False


@pytest.fixture
def v1():
    return Vector([1, 2, 3])


@pytest.fixture
def v2():
    return Vector([-1, 0.50, 10])


@pytest.fixture
def v0():
    return Vector([0,] * 3)


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
    # Dot Product

    @pytest.mark.xfail(reason="Not implemented", run=False)
    def test_not_implemented(self, v1, v2):
        with pytest.raises(NotImplementedError) as excinfo:
            v1 * v2
        assert "NotImplementedError" in str(excinfo)

    def test_mul_self(self, v1, v2):
        assert 014.00 == v1 * v1
        assert 101.25 == v2 * v2

    def test_mul(self, v1, v2):
        assert 30 == v1 * v2

    def test_zero_vector(self, v1, v2, v0):
        assert 0 == v0 * v1
        assert 0 == v0 * v2

    def test_communitive_property(self, v1, v2):
        assert v1 * v2 == v2 * v1

    def test_not_vector(self, v1, not_vectors):
        for value in not_vectors:
            with pytest.raises(TypeError) as excinfo:
                new_v = v1 * value
            assert (
                f"Expected Type 'Vector' or 'numbers.real', got type '{type(value)}'."
                == str(excinfo.value)
            )

    def test_diff_dim(self, v1):
        v = Vector([3,] * 5)
        with pytest.raises(DimensionError) as excinfo:
            v * v1
        assert (
            f"Cannot compute dot product between Vector with self.dimension=5 and Vector with other.dimension=3."
            == str(excinfo.value)
        )


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


class TestAngle:
    def test_vaild(self, v1, v2):
        assert 0.6487840721271294 == pytest.approx(v1.angle(v2))
        assert 37.1726 == pytest.approx(v1.angle(v2, unit="degrees"))

    def test_parallel(self, v1):
        v = Vector([5, 10, 15])
        assert 0 == pytest.approx(v1.angle(v))
        assert 0 == pytest.approx(v1.angle(v, unit="degrees"))

    def test_perpendicular(self):
        v = Vector([1, 0, 0])
        u = Vector([0, 1, 0])
        assert 1.570796326 == pytest.approx(v.angle(u))
        assert 90 == pytest.approx(v.angle(u, unit="degrees"))

    def test_opposite(self):
        v = Vector([1, 0, 0])
        u = Vector([-1, 0, 0])
        assert pi == pytest.approx(v.angle(u))
        assert 180 == pytest.approx(v.angle(u, unit="degrees"))

    def test_communitive_property(self, v1, v2):
        assert v1.angle(v2) == v2.angle(v1)


class TestIsParallel:
    def test_is_not_parallel(self):
        v = Vector([1, 0])
        w = Vector([0, 1])
        assert not v.is_parallel(w)
        assert not w.is_parallel(v)

    def test_is_parallel_1(self):
        v = Vector([1, 1])
        w = Vector([3, 3])
        assert v.is_parallel(w)
        assert w.is_parallel(v)

    def test_is_parallel_2(self):
        v = Vector([1, 1])
        w = Vector([-3, -3])
        assert v.is_parallel(w)
        assert w.is_parallel(v)

    def test_example_1(self):
        v = Vector([-7.579, -7.88])
        w = Vector([22.737, 23.64])
        assert v.is_parallel(w)
        assert w.is_parallel(v)

    def test_example_2(self):
        v = Vector([-2.029, 9.97, 4.172])
        w = Vector([-9.231, -6.639, -7.245])
        assert not v.is_parallel(w)
        assert not w.is_parallel(v)

    def test_example_3(self):
        v = Vector([-2.328, -7.284, -1.214])
        w = Vector([-1.821, 1.072, -2.94])
        assert not v.is_parallel(w)
        assert not w.is_parallel(v)

    def test_example_4(self):
        v = Vector([2.118, 4.827])
        w = Vector([0, 0])
        assert v.is_parallel(w)
        assert w.is_parallel(v)


class TestIsOrthogonal:
    def test_is_orthogonal(self):
        v = Vector([1, 0])
        w = Vector([0, 1])
        assert v.is_orthogonal(w)
        assert w.is_orthogonal(v)

    def test_is_not_othogonal(self):
        v = Vector([1, 1])
        w = Vector([3, 3])
        assert not v.is_orthogonal(w)
        assert not w.is_orthogonal(v)

    def test_example_1(self):
        v = Vector([-7.579, -7.88])
        w = Vector([22.737, 23.64])
        assert not v.is_orthogonal(w)
        assert not w.is_orthogonal(v)

    def test_example_2(self):
        v = Vector([-2.029, 9.97, 4.172])
        w = Vector([-9.231, -6.639, -7.245])
        assert not v.is_orthogonal(w)
        assert not w.is_orthogonal(v)

    def test_example_3(self):
        v = Vector([-2.328, -7.284, -1.214])
        w = Vector([-1.821, 1.072, -2.940])
        assert v.is_orthogonal(w)
        assert w.is_orthogonal(v)

    def test_example_4(self):
        v = Vector([2.118, 4.827])
        w = Vector([0, 0])
        assert v.is_orthogonal(w)
        assert w.is_orthogonal(v)


class TestParallelComponent:
    def test_parallel_componet_x(self, v1):
        b = Vector([1, 0, 0])
        assert (1, 0, 0) == v1.parallel_component(b).coords

    def test_parallel_componet_y(self, v1):
        b = Vector([0, 1, 0])
        assert (0, 2, 0) == v1.parallel_component(b).coords

    def test_parallel_componet_z(self, v1):
        b = Vector([0, 0, 1])
        assert (0, 0, 3) == v1.parallel_component(b).coords

    def test_example(self):
        v = Vector([3.039, 1.879])
        b = Vector([0.825, 2.036])
        assert (1.0826069624844668, 2.671742758325302) == v.parallel_component(b).coords


class TestOthogonalComponent:
    def test_orthogonal_componet_x(self, v1):
        b = Vector([1, 0, 0])
        assert (0, 2, 3) == v1.orthogonal_component(b).coords

    def test_orthogonal_componet_y(self, v1):
        b = Vector([0, 1, 0])
        assert (1, 0, 3) == v1.orthogonal_component(b).coords

    def test_orthogonal_componet_z(self, v1):
        b = Vector([0, 0, 1])
        assert (1, 2, 0) == v1.orthogonal_component(b).coords

    def test_example(self):
        v = Vector([-9.88, -3.264, -8.159])
        b = Vector([-2.155, -9.353, -9.473])
        assert (
            -8.350081043195763,
            3.376061254287722,
            -1.4337460427811841,
        ) == v.orthogonal_component(b).coords


class TestComponents:
    def test_componets_x(self, v1):
        b = Vector([1, 0, 0])
        cs = v1.components(b)
        assert (0, 2, 3) == cs["othogonal"].coords
        assert (1, 0, 0) == cs["parallel"].coords

    def test_componets_y(self, v1):
        b = Vector([0, 1, 0])
        cs = v1.components(b)
        assert (1, 0, 3) == cs["othogonal"].coords
        assert (0, 2, 0) == cs["parallel"].coords

    def test_componets_z(self, v1):
        b = Vector([0, 0, 1])
        cs = v1.components(b)
        assert (1, 2, 0) == cs["othogonal"].coords
        assert (0, 0, 3) == cs["parallel"].coords

    def test_example(self):
        v = Vector([3.009, -6.172, 3.692, -2.51])
        b = Vector([6.404, -9.144, 2.759, 8.718])
        cs = v.components(b)
        assert (
            1.04048383278591,
            -3.3612392515606433,
            2.8439150366421497,
            -5.189813233256158,
        ) == cs["othogonal"].coords
        assert (
            1.9685161672140898,
            -2.8107607484393564,
            0.8480849633578503,
            2.679813233256158,
        ) == cs["parallel"].coords


class TestCrossProduct:
    def test_zero_vector(self, v1, v0):
        result = v1.cross_product(v0)
        assert (0, 0, 0) == result.coords

    def test_vaild_vectors(self):
        v = Vector([1, 7, 74])
        u = Vector([-26, -4, 5])
        result = v.cross_product(u)
        assert (331, -1929, 178) == result.coords

    def test_example_1(self):
        v = Vector([8.462, 7.893, -8.187])
        u = Vector([6.984, -5.975, 4.778])
        result = v.cross_product(u)
        assert (-11.204570999999994, -97.609444, -105.68516199999999) == result.coords

    def test_example_2(self):
        v = Vector([-8.987, -9.838, 5.031])
        u = Vector([-4.268, -1.861, -8.866])
        result = v.cross_product(u)
        assert (96.58639899999999, -101.15105, -25.263776999999997) == result.coords

    def test_example_3(self):
        v = Vector([1.5, 9.547, 3.691])
        u = Vector([-6.007, 0.124, 5.772])
        result = v.cross_product(u)
        assert (54.647600000000004, -30.829836999999998, 57.534829) == result.coords


class TestArea:
    def test_zero_vector(self, v1, v0):
        assert 0 == v1.area(v0)

    def test_valid_vectors(self):
        v = Vector([1, 7, 74])
        u = Vector([-26, -4, 5])
        assert 1965.2699560111328 == v.area(u)

    def test_example_1(self):
        v = Vector([8.462, 7.893, -8.187])
        u = Vector([6.984, -5.975, 4.778])
        assert 144.30003269663322 == v.area(u)

    def test_example_2(self):
        v = Vector([-8.987, -9.838, 5.031])
        u = Vector([-4.268, -1.861, -8.866])
        assert 142.12222140184633 == v.area(u)

    def test_example_3(self):
        v = Vector([1.5, 9.547, 3.691])
        u = Vector([-6.007, 0.124, 5.772])
        assert 42.56493739941894 == v.area(u) / 2
