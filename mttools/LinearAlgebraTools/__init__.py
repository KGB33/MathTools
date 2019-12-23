from mttools.utils.Exceptions import (
    InconsistentWarning,
    InfiniteSolutionsWaring,
    UnderDeterminedError,
)

from .Matrix import Matrix


def solve_linear_equations(*args):
    """
    Solves a system of linear equations

    :param args: (dicts)
        {variable: coefficient} pairs, one dictionary per equation
        if a coefficient is zero it NEEDS to be in the dict.
        the last key: value pair should be the solution (RH) of the equation

    :return: (dict)
        {variable: value} pairs
    """
    # Check to see if solution is underdetermined (num_eq < num_var)
    if len(args) < len(args[0]) - 1:  # -1 for sol key
        raise UnderDeterminedError

    # Create solution dict
    solution = {key: None for key in args[0]}
    del solution["sol"]  # removes unneeded key

    # Convert Dicts to matrix
    to_array = []
    for equation in args:
        to_row = []
        for variable in equation:
            to_row.append(equation[variable])
        to_array.append(to_row)
    m = Matrix(to_array)

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
    for row in m.array:
        variable_key = None
        for value, key in zip(row, solution):
            if value == 1:
                variable_key = key
        solution.update({variable_key: row[-1]})

    # Return solution
    return solution
