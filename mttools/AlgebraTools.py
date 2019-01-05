import numpy as np

def quadratic_formula(a, b, c):
    """
    Calculates the roots of a quadratic equation and returns them as a tuple

    :param a: (numeric)
        Coefficient of the x-squared term
    :param b: (numeric)
        Coefficient of the x term
    :param c: (numeric)
        Coefficient of the x-less term

    :return:
        Roots, as a tuple
    """
    # Calculate determinate
    det = pow(b, 2) - 4 * a * c

    # 3 Cases
    if det > 0:  # Two real solutions
        solutions = ((-b + np.sqrt(det))/(2 * a), (-b - np.sqrt(det))/(2 * a))
    elif det == 0:  # One Real solution
        solutions = (-b/(2 * a),)
    elif det < 0:  # Two complex solutions

        solutions = (complex(-b / (2 * a), + np.sqrt(-det)/(2 * a)),
                     complex(-b / (2 * a), - np.sqrt(-det)/(2 * a)),)
    return solutions
