"""
A Collection of tools related to the number theory branch of mathmatics.
These include Primes, Greatest Common Factors, etc. 
"""

from math import sqrt

from typing import List


def perfect_factors(n: int) -> List[int]:
    """
    Generates perfect factors of number starting with 1

    n: number to find the factors of

    return: a sorted List of the Perfect Factors
    """
    # 1 and n are always divisors
    factors = [1, n]

    largest = int(sqrt(n))

    # special-case square numbers to avoid adding the same divisor twice
    if largest * largest == n:
        factors.append(largest)
    else:
        largest += 1

    # all other divisors
    for i in range(2, largest):
        if n % i == 0:
            factors.append(i)
            factors.append(n // i)

    return sorted(factors)


def gcd(a: int, b: int) -> int:
    """
    Finds the Greatest Common Divisor of two integers.
    """
    a, b = abs(a), abs(b)
    # Simple cases
    if b == 0:
        return a

    if a == 0:
        return b

    sort = sorted([a, b])
    if sort[1] % sort[0] == 0:
        return sort[0]
    return gcd(b, a % b)


def lcm(a: int, b: int) -> int:
    """
    Finds the Least Common Multiple of two integers.
    """
    return (a * b) / gcd(a, b)
