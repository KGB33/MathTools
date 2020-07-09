import pytest

from mttools.utils.exceptions import (
    InconsistentWarning,
    InfiniteSolutionsWaring,
    UnderDeterminedError,
)
from mttools.linear_algebra_tools import solve_linear_equations


class TestLinearEquationSolver:
    def test_3eq_3unk_1sol(self):
        eq_1 = [3, 2, -2, 9]
        eq_2 = [0, 4, 0, 8]
        eq_3 = [7, -2, 1, 19]
        expected = [3, 2, 2]
        solution = solve_linear_equations(eq_1, eq_2, eq_3)
        assert expected == solution

    def test_2eq_2unk_0sol(self):
        eq_1 = [2, -1, 4]
        eq_2 = [6, -3, 3]
        with pytest.raises(InconsistentWarning):
            solution = solve_linear_equations(eq_1, eq_2)
            assert {} == solution

    def test_2eq_2unk_inf_sol(self):
        eq_1 = [2, -1, 4]
        eq_2 = [6, -3, 12]
        with pytest.raises(InfiniteSolutionsWaring):
            solution = solve_linear_equations(eq_1, eq_2)

    def test_underdetermined(self):
        eq_1 = [3, 2, -2, 9]
        eq_2 = [0, 4, 0, 8]
        with pytest.raises(UnderDeterminedError):
            solve_linear_equations(eq_1, eq_2)
