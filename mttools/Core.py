from math import inf


def check_inf(val):
    if abs(val) == 9.999999999999999e29:
        return inf * val
    return val
