from math import sqrt


def perfect_factors(n):
    """
    Generates perfect factors of number starting with 1

    :param n: (int)
        number to find the factors of
    :yields: (int)
        next factor
    """
    # "1" is always a divisor
    yield 1
    # likewise n is always a divisor
    yield n

    largest = int(sqrt(n))

    # special-case square numbers to avoid yielding the same divisor twice
    if largest * largest == n:
        yield largest
    else:
        largest += 1

    # all other divisors
    for i in range(2, largest):
        if n % i == 0:
            yield i
            yield n / i


def gcd(a, b):
    a, b = abs(a), abs(b)
    # Simple cases
    if b == 0:
        return a
    elif a == 0:
        return b

    sort = sorted([a, b])
    if sort[1] % sort[0] == 0:
        return sort[0]
    else:
        return gcd(b, a % b)


def lcf(a, b):
    pass


def lcm(a, b):
    pass
