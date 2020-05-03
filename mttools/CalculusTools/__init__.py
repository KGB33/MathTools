from mttools.Constants import EPSILON
from mttools.Core import check_inf


def derivative(f):
    """
    Takes a lambda function and returns the derivative as a lambda function
    :param f: A one dimensional lambda function
    :return: f'(x)
    """
    g = lambda x, h: f(x + h)
    return limit(())
    # TODO Diferentiation


def limit(f, a):
    """
    Takes the limit of some lambda function, f, as f approaches a
    :param f: function
    :param a: value f tends towards
    :return: limit of f
    """
    try:
        return f(a)  # if the function exists at a it tends to f(a)
    except ZeroDivisionError:
        if abs(f(a - EPSILON) - f(a + EPSILON)) <= pow(10, -10):
            return check_inf(f(a + EPSILON))
        return None


def function_roots(f):
    """
    Uses Newton's method to find the roots of a function
    :param f: function
    :return: (roots, )
    """
    pass
