
from math import sqrt


def factors(x, sort=False):
    results = set()
    for x1 in range(1, int(sqrt(x)+1)):
        if x % x1 == 0:
            results.add(x1)
            results.add(x // x1)

    results = list(results)
    return sorted(results) if sort else results


def proper_factors(x):
    return factors(x, True)[:-1]


def non_trivial_factors(x):
    return factors(x, True)[1:-1]


def is_prime(x):
    return len(factors(x)) == 2
