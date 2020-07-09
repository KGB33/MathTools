from mttools.utils.exceptions import (
    InconsistentWarning,
    InfiniteSolutionsWaring,
    UnderDeterminedError,
)

from .matrix import Matrix

from typing import List
from mttools.utils.types import RealNumber


def solve_linear_equations(*args: List[RealNumber]) -> List[RealNumber]:
    """
    Solves a system of linear equations

    params:
        args:
            An ordered list of the coefficients for an equation, 
            where the last number is the RH side

    return:
        The Solutions to the system of linear equations

    Example:

        If the first equation is:
            3a + 2b + ... -3n = 12
        the corresponding arg would be:
            [3, 2, ..., -3, 12]
    """
    # Check to see if solution is underdetermined (num_eq < num_var)
    if len(args) < len(args[0]) - 1:  # -1 because the RH side is not a variable
        raise UnderDeterminedError

    m = Matrix(list(args))

    # Put Matrix in Reduced-Row Echelon Form
    m.rref()

    # Check matrix for num_solutions
    inf_sol = [0 for _ in range(m.num_columns)]
    no_sol = inf_sol[:-1] + [1]
    for row in m.array:
        if row == inf_sol:
            raise InfiniteSolutionsWaring
        elif row == no_sol:
            raise InconsistentWarning

    # Convert matrix to solution dict
    solution = []
    for row in m.array:
        solution.append(row[-1])

    # Return solution
    return solution
