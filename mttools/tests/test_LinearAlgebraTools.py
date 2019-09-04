import pytest

from mttools.Exceptions import (
    DimensionError,
    InconsistentWarning,
    InfiniteSolutionsWaring,
    NoInverseWarning,
    UnderDeterminedError,
)
from mttools.LinearAlgebraTools import Matrix, solve_linear_equations, SquareMatrix


class TestMatrix:
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

    def test_str(self):
        m = Matrix([[1, 2], [1, 2], [1, 2]])
        expected = "[ 1, 2, ]\n[ 1, 2, ]\n[ 1, 2, ]\n"
        assert expected == str(m)

    def test_mul_bad_size(self):
        m = Matrix([[1, 2], [1, 2], [1, 2]])  # 3x2
        n = Matrix([[1], [2], [3]])  # 3x1
        with pytest.raises(DimensionError):
            m * n

    def test_mul_valid_size(self):
        m = Matrix([[1, 2], [1, 2], [1, 2]])  # 3x2
        n = SquareMatrix([[1, 2], [3, 4]])  # 2x2
        expected = [[7, 10], [7, 10], [7, 10]]
        assert expected == (m * n).array

    def test_mul_same_size(self):
        m = SquareMatrix([[1, 2], [3, 4]])
        n = SquareMatrix([[1, 2], [3, 4]])
        expected = SquareMatrix(([[7, 10], [15, 22]]))
        assert expected.array == (m * n).array

    def test_scalar_mul(self):
        m = SquareMatrix([[1, 2], [3, 4]])
        m.scalar_multiplication(2)
        expected = SquareMatrix([[2, 4], [6, 8]])
        assert expected.array == m.array

    def test_add_bad_size(self):
        m = Matrix([[1, 2], [1, 2], [1, 2]])  # 3x2
        n = SquareMatrix([[1, 2], [3, 4]])  # 2x2
        with pytest.raises(DimensionError):
            m + n

    def test_add(self):
        m = Matrix([[1, 2], [3, 4]])  # 2x2
        n = SquareMatrix([[1, 2], [3, 4]])  # 2x2
        expected = Matrix([[2, 4], [6, 8]])
        assert expected.array == (m + n).array

    def test_rank(self):
        m = Matrix([[1, 2], [3, 4], [2, 5]])
        assert 2 == m.rank()

    def test_transpose_2_3(self):
        m = Matrix([[1, 2, 3], [8, 9, 0]])
        m.transpose()
        assert [[1, 8], [2, 9], [3, 0]] == m.array

    def test_transpose_3_2(self):
        m = Matrix([[1, 8], [2, 9], [3, 0]])
        m.transpose()
        assert [[1, 2, 3], [8, 9, 0]] == m.array

    def test_swap_rows(self):
        m = Matrix([[1, 2, 3], [8, 9, 0]])
        m.swap_rows(0, 1)
        assert [[8, 9, 0], [1, 2, 3]] == m.array

    def test_multiply_row(self):
        m = Matrix([[1, 2, 3], [8, 9, 0]])
        m.multiply_row(0, 3)
        assert [[3, 6, 9], [8, 9, 0]] == m.array

    def test_add_row_no_scalar(self):
        m = Matrix([[1, 2, 3], [8, 9, 0]])
        m.add_rows(1, 0)
        assert [[9, 11, 3], [8, 9, 0]] == m.array

    def test_add_row_with_scalar(self):
        m = Matrix([[1, 2, 3], [8, 9, 0]])
        m.add_rows(0, 1, scalar=3)
        assert [[1, 2, 3], [11, 15, 9]] == m.array

    def test_rref_2_3(self):
        m = Matrix([[1, 2, 3], [8, 9, 3]])
        m.rref()
        assert [[1, 0, -3], [0, 1, 3]] == m.array

    def test_rref_3_3(self):
        m = Matrix([[0, 1, 2], [1, 2, 1], [2, 7, 8]])
        m.rref()
        expected = [[1, 0, -3], [0, 1, 2], [0, 0, 0]]
        assert expected == m.array


class TestSquareMatrix:
    def test_init_square_array(self):
        m = SquareMatrix([[1, 2], [3, 4]])
        assert [[1, 2], [3, 4]] == m.array
        assert 2 == m.num_columns
        assert 2 == m.num_rows

    def test_init_non_square_array(self):
        with pytest.raises(DimensionError):
            m = SquareMatrix([[1, 2, 3], [1, 2]])

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

    def test_rref_to_id(self):
        m = SquareMatrix([[1, 2, 3], [3, 4, 5], [5, 8, 7]])
        m.rref()
        assert m.identity_matrix().array == m.array

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

    def test_determinate_2_2(self):
        m = SquareMatrix([[1, 2], [3, 4]])
        assert -2 == m.determinate()

    def test_determinate_3_3(self):
        m = SquareMatrix([[1, 3, 2], [4, 1, 3], [2, 5, 2]])
        assert 17 == m.determinate()

    def test_determinate_4_4(self):
        m = SquareMatrix([[1, 3, 2, 5], [4, 1, 3, 5], [2, 5, 2, 5], [3, 4, 5, 6]])
        assert -88 == m.determinate()

    def test_trace(self):
        m = SquareMatrix([[1, 2], [3, 4]])
        assert 5 == m.trace()


class TestLinearEquationSolver:
    def test_3eq_3unk_1sol(self):
        eq_1 = {"a": 3, "b": 2, "c": -2, "sol": 9}
        eq_2 = {"a": 0, "b": 4, "c": 0, "sol": 8}
        eq_3 = {"a": 7, "b": -2, "c": 1, "sol": 19}
        expected = {"a": 3, "b": 2, "c": 2}
        solution = solve_linear_equations(eq_1, eq_2, eq_3)
        assert expected == solution

    def test_2eq_2unk_0sol(self):
        eq_1 = {"a": 2, "b": -1, "sol": 4}
        eq_2 = {"a": 6, "b": -3, "sol": 3}
        with pytest.raises(InconsistentWarning):
            solution = solve_linear_equations(eq_1, eq_2)
            assert {} == solution

    def test_2eq_2unk_inf_sol(self):
        eq_1 = {"a": 2, "b": -1, "sol": 4}
        eq_2 = {"a": 6, "b": -3, "sol": 12}
        with pytest.raises(InfiniteSolutionsWaring):
            solution = solve_linear_equations(eq_1, eq_2)

    def test_underdetermined(self):
        eq_1 = {"a": 3, "b": 2, "c": -2, "sol": 9}
        eq_2 = {"a": 0, "b": 4, "c": 0, "sol": 8}
        with pytest.raises(UnderDeterminedError):
            solve_linear_equations(eq_1, eq_2)
