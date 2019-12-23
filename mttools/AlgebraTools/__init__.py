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
        solutions = ((-b + sqrt(det)) / (2 * a), (-b - sqrt(det)) / (2 * a))
    elif det == 0:  # One Real solution
        solutions = (-b / (2 * a),)
    elif det < 0:  # Two complex solutions

        solutions = (
            complex(-b / (2 * a), +sqrt(-det) / (2 * a)),
            complex(-b / (2 * a), -sqrt(-det) / (2 * a)),
        )
    return solutions


def sqrt(num):
    """
    Calculates the Square root of num

    :param num: Number
    :return: Square root of num
    """
    # Checks if num is equal to zero
    if num == 0:
        return 0
    elif num < 0:
        num = num * -1
        is_negative = True
    else:
        is_negative = False

    # Newton/babylonian method
    max_iterations = 20  # Number of correct digits is approx doubled each iteration
    r = num / 2
    for _ in range(0, max_iterations):
        r = 0.5 * (r + num / r)

    if is_negative:
        return r * 1j
    return r
