import pytest

from mttools.LinearAlgebraTools.Matrix import Matrix
from mttools.utils.Exceptions import DimensionError


class TestInit:
    def test_init_good_array(self):
        m = Matrix([[1, 2], [1, 2], [1, 2]])
        assert [[1, 2], [1, 2], [1, 2]] == m.array
        assert 3 == m.num_rows
        assert 2 == m.num_columns

    def test_init_bad_array_unequal_col(self):
        with pytest.raises(DimensionError):
            m = Matrix([[1, 2, 3], [1, 2], [1, 2]])

    def test_init_bad_array_unequal_row(self):
        with pytest.raises(DimensionError):
            m = Matrix([[1, 2], [1, 2], [1]])


class TestStr:
    def test_str(self):
        m = Matrix([[1, 2], [1, 2], [1, 2]])
        expected = "[ 1, 2, ]\n[ 1, 2, ]\n[ 1, 2, ]\n"
        assert expected == str(m)


class TestMul:
    def test_mul_bad_size(self):
        m = Matrix([[1, 2], [1, 2], [1, 2]])  # 3x2
        n = Matrix([[1], [2], [3]])  # 3x1
        with pytest.raises(DimensionError):
            m * n

    def test_mul_valid_size(self):
        m = Matrix([[1, 2], [1, 2], [1, 2]])  # 3x2
        n = Matrix([[1, 2], [3, 4]])  # 2x2
        expected = [[7, 10], [7, 10], [7, 10]]
        assert expected == (m * n).array

    def test_mul_same_size(self):
        m = Matrix([[1, 2], [3, 4]])
        n = Matrix([[1, 2], [3, 4]])
        expected = Matrix(([[7, 10], [15, 22]]))
        assert expected.array == (m * n).array


class TestScalarMul:
    def test_scalar_mul(self):
        m = Matrix([[1, 2], [3, 4]])
        m.scalar_multiplication(2)
        expected = Matrix([[2, 4], [6, 8]])
        assert expected.array == m.array


class TestAdd:
    def test_add_bad_size(self):
        m = Matrix([[1, 2], [1, 2], [1, 2]])  # 3x2
        n = Matrix([[1, 2], [3, 4]])  # 2x2
        with pytest.raises(DimensionError):
            m + n

    def test_add(self):
        m = Matrix([[1, 2], [3, 4]])  # 2x2
        n = Matrix([[1, 2], [3, 4]])  # 2x2
        expected = Matrix([[2, 4], [6, 8]])
        assert expected.array == (m + n).array


class TestRank:
    def test_rank(self):
        m = Matrix([[1, 2], [3, 4], [2, 5]])
        assert 2 == m.rank()


class TestTranspose:
    def test_transpose_2_3(self):
        m = Matrix([[1, 2, 3], [8, 9, 0]])
        m.transpose()
        assert [[1, 8], [2, 9], [3, 0]] == m.array

    def test_transpose_3_2(self):
        m = Matrix([[1, 8], [2, 9], [3, 0]])
        m.transpose()
        assert [[1, 2, 3], [8, 9, 0]] == m.array


class TestSwapRows:
    def test_swap_rows(self):
        m = Matrix([[1, 2, 3], [8, 9, 0]])
        m.swap_rows(0, 1)
        assert [[8, 9, 0], [1, 2, 3]] == m.array


class TestMulRows:
    def test_multiply_row(self):
        m = Matrix([[1, 2, 3], [8, 9, 0]])
        m.multiply_row(0, 3)
        assert [[3, 6, 9], [8, 9, 0]] == m.array


class TestAddRows:
    def test_add_row_no_scalar(self):
        m = Matrix([[1, 2, 3], [8, 9, 0]])
        m.add_rows(1, 0)
        assert [[9, 11, 3], [8, 9, 0]] == m.array

    def test_add_row_with_scalar(self):
        m = Matrix([[1, 2, 3], [8, 9, 0]])
        m.add_rows(0, 1, scalar=3)
        assert [[1, 2, 3], [11, 15, 9]] == m.array


class TestRREF:
    def test_rref_2_3(self):
        m = Matrix([[1, 2, 3], [8, 9, 3]])
        m.rref()
        assert [[1, 0, -3], [0, 1, 3]] == m.array

    def test_rref_3_3(self):
        m = Matrix([[0, 1, 2], [1, 2, 1], [2, 7, 8]])
        m.rref()
        expected = [[1, 0, -3], [0, 1, 2], [0, 0, 0]]
        assert expected == m.array
