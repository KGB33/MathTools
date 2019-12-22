import pytest

from mttools.Exceptions import (
    DimensionError,
    InconsistentWarning,
    InfiniteSolutionsWaring,
    NoInverseWarning,
    UnderDeterminedError,
)
from mttools.LinearAlgebraTools import solve_linear_equations


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
