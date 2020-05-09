import random

from typing import List, Dict, Optional, cast
from mttools.Constants import Prime


def fermat_primality_test(p: int, num_trials: int) -> bool:
    """
    Uses Fermat's Little Theorem to test for possible primality.
        If this returns False, p is guaranteed to be composite
        If this returns True, p is probably, but not guaranteed to be prime.

    Params:
        p: Number that is being tested for primality.
        num_trials: Number of times to run the test.
    """
    # Checks to see if p < 2:
    if p < 2:
        return False

    # Checks To see if p is a carmichael number
    carmichael_numbers = {
        561,
        1105,
        1729,
        2465,
        2821,
        6601,
        8911,
        10585,
        15841,
        29341,
        41041,
        46657,
        52633,
        62745,
        63973,
        75361,
        101101,
        115921,
        126217,
        162401,
        172081,
        188461,
        252601,
        278545,
        294409,
        314821,
        334153,
        340561,
        399001,
        410041,
        449065,
        488881,
        512461,
    }
    if p in carmichael_numbers:
        return False

    # Fermat's Little Theorem
    for _ in range(num_trials):
        base = random.randint(2, p - 1)
        if pow(base, p - 1) % p != 1:
            return False
    return True


def division_primality_test(p: int) -> bool:
    """
    Standard division test for primality

    params: 
        p: Number that is being tested for primality
    """
    # negatives, 0, 1 are not prime
    if p < 2:
        return False

    # Checks divisors from 3 to p/2
    for divisor in range(2, int(p / 2) + 1):
        if p % divisor == 0:
            return False

    return True


def sieve_of_eratosthenes(upper_bound: int) -> List[Prime]:
    """
    Creates a Sieve of Eratosthenes from 0 to upper_bound

    params:
        upper_bound: Upper-Bound for the sieve

    return:
        Ordered list of all primes less than upper_bound
    """

    # Assume everything is prime, except 0 and 1
    sieve = [True for _ in range(upper_bound)]
    sieve[0] = False
    sieve[1] = False

    # Iterate over sieve
    for i, is_prime in enumerate(sieve):
        try:
            if is_prime:
                j = i * i
            while j < upper_bound:
                sieve[j] = False
                j += i
        except UnboundLocalError:
            pass

    return sorted([i for i, is_prime in enumerate(sieve) if is_prime])


def prime_factors(num: int) -> Dict[Prime, int]:
    """
    Creates a dictionary of prime factors for a given number.

    params
        num: Number to be factored

    return:
        Dictionary of where the keys are prime factors and the values are their respective powers.

    Example:

        36 = 2^2 * 3^2

        >>> prime_factors(36)
        {2: 2, 3: 2,}
    """
    n: Prime = 2
    result: Dict[Prime, int] = {}
    while n <= num:
        if num % n == 0:
            num = num // n
            if n in result:
                result[n] += 1
            else:
                result.update({n: 1})
        else:
            n += 1
    return result


def largest_prime_less_than(num: int) -> Optional[int]:
    """
    Returns the largest prime less than Num,
    if there are no primes less than num, returns None

    params
        num: Number to search for primes below

    return:
        Largest prime less than num, if such a prime does not exist, returns None
    """
    for i in range((num - 1), 0, -1):
        if division_primality_test(i):
            return i
    else:
        return None
