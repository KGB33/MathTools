import pytest

from mttools.LinearAlgebraTools import SquareMatrix
from mttools.Exceptions import DimensionError, NoInverseWarning


class TestInit:
    def test_init_square_array(self):
        m = SquareMatrix([[1, 2], [3, 4]])
        assert [[1, 2], [3, 4]] == m.array
        assert 2 == m.num_columns
        assert 2 == m.num_rows

    def test_init_non_square_array(self):
        with pytest.raises(DimensionError):
            m = SquareMatrix([[1, 2, 3], [1, 2]])


class TestInverse:
    def test_inverse(self):
        m = SquareMatrix([[1, 2], [3, 4]])
        m.inverse()
        expected = SquareMatrix([[-2, 1], [3 / 2, -1 / 2]])
        assert expected.array == m.array

    def test_inverse_no_inverse(self):
        m = SquareMatrix([[1, 2], [1, 2]])
        with pytest.raises(NoInverseWarning):
            m.inverse()
        assert [[1, 2], [1, 2]] == m.array


class TestIdenity:
    def test_rref_to_id(self):
        m = SquareMatrix([[1, 2, 3], [3, 4, 5], [5, 8, 7]])
        m.rref()
        assert m.identity_matrix().array == m.array


class TestMinor:
    def test_minor_2_2(self):
        m = SquareMatrix([[1, 2], [3, 4]])
        assert 1 == m.minor(2, 2)

    def test_minor_3_3(self):
        m = SquareMatrix([[1, 3, 2], [4, 1, 3], [2, 5, 2]])
        assert [[3, 2], [5, 2]] == m.minor(2, 1).array

    def test_minor_4_4(self):
        m = SquareMatrix([[1, 3, 2, 5], [4, 1, 3, 5], [2, 5, 2, 5], [3, 4, 5, 6]])
        expected = [[1, 3, 2], [4, 1, 3], [2, 5, 2]]
        assert expected == m.minor(4, 4).array


class TestDeterminate:
    def test_determinate_2_2(self):
        m = SquareMatrix([[1, 2], [3, 4]])
        assert -2 == m.determinate()

    def test_determinate_3_3(self):
        m = SquareMatrix([[1, 3, 2], [4, 1, 3], [2, 5, 2]])
        assert 17 == m.determinate()

    def test_determinate_4_4(self):
        m = SquareMatrix([[1, 3, 2, 5], [4, 1, 3, 5], [2, 5, 2, 5], [3, 4, 5, 6]])
        assert -88 == m.determinate()


class TestTrace:
    def test_trace(self):
        m = SquareMatrix([[1, 2], [3, 4]])
        assert 5 == m.trace()
