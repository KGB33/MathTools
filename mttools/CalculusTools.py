import math

def derivative(f):
    """
    Takes a lambda function and returns the derivative as a lambda function
    :param f: A one dimensional lambda function
    :return: f'(x)
    """
    g = lambda x, h: f(x + h)
    return(limit(()))
    # TODO Diferentiation


def limit(f, a, diff_1=pow(10, -5), diff_2=pow(10, -10)):
    """
    Takes the limit of some lambda function, f, as f approaches a
    :param f: lambda function
    :param a: limit
    :param diff_1: 1st Difference checked on the RH/LH side for continuity, default is 10^-5
    :param diff_2: 2nd Difference checked on the RH/LH side for continuity, default is 10^-10
    :return: limit of f
    """
    f_right = f(a + diff_1)
    f_left = f(a - diff_1)
    if abs(f_left - f_right) < pow(10, -3):
        if f(a + diff_2) / 2 > f_right:
            if f_right > 0:
                return math.inf
            return -math.inf
        return (f_right + f_left) / 2


def function_roots(f):
    """
    Uses Newton's method to find the roots of a function
    :param f: function
    :return: (roots, )
    """
    pass