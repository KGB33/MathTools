import random


def fermat_primality_test(p, num_trials):
    """
    Uses Fermat's Little Theorem to test for possible primality.
        If this returns False, p is guaranteed to be composite
        If this returns True, p is probably, but not guaranteed to be prime.

    :param p: (int)
        Number that is being tested for primality

    :param num_trials: (int)
        Number of times to run the test

    :return: (boolean)
        False if composite
        True if probably Prime
    """
    # Checks to see if p < 2:
    if p < 2:
        return False

    # Checks To see if p is a carmichael number
    carmichael_numbers = {561, 1105, 1729, 2465, 2821, 6601, 8911,
                           10585, 15841, 29341, 41041, 46657, 52633,
                           62745, 63973, 75361, 101101, 115921, 126217,
                           162401, 172081, 188461, 252601, 278545, 294409,
                           314821, 334153, 340561, 399001, 410041, 449065,
                           488881, 512461}
    if p in carmichael_numbers:
        return False

    # Fermat's Little Theorem
    for _ in range(num_trials):
        base = random.randint(2, p - 1)
        if pow(base, p - 1) % p != 1:
            return False
    return True


def division_primality_test(p):
    """
    Standard division test for primality

    :param p: (int)
        Number that is being tested for primality

    :return: (boolean)
        True if Prime
        False if Composite
    """
    # negatives, 0, 1 are not prime
    if p < 2:
        return False

    # Checks divisors from 3 to p/2
    for divisor in range(2, int(p / 2) + 1):
        if p % divisor == 0:
            return False

    return True


def sieve_of_eratosthenes(upper_bound):
    """
    Creates a Sieve of Eratosthenes from 0 to upper_bound

    :param upper_bound: (int)
        Upper-Bound for the sieve

    :return: (set)
        Ordered set of all primes less than upper_bound
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

    # Remove non-primes and turn into set
    result = []
    for p, is_prime in enumerate(sieve):
        if is_prime:
            result.append(p)
    return set(result)


def prime_factors(num):
    """
    Creates a dictionary of prime factors where:
        {factor: power}

    :param num: (int)
        Number to be factored

    :return: (dict)
        Dictionary of prime factors
    """
    n = 2
    dic = {}
    while n <= num:
        if num % n == 0:
            num = num / n
            if n in dic:
                dic[n] += 1
            else:
                dic.update({n: 1})
        else:
            n += 1
    return dic


def largest_prime_less_than(num):
    """
    Returns the largest prime less than Num,
    if there are no primes less than num, returns None

    :param num: (int)
        Number to search for primes below

    :return: (int)
        largest prime less than num
    """
    for i in range((num - 1), 0, -1):
        if division_primality_test(i):
            return i
    else:
        return None






