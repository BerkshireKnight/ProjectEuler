
from math import sqrt


def factors(x, sorted=False):
    results = []
    for x1 in range(1, int(sqrt(x)+2)):
        if x % x1 == 0:
            results.append(x1)
            results.append(x // x1)

    return sorted(results) if sorted else results


def proper_factors(x):
    return factors(x, True)[1:]


def non_trivial_factors(x):
    return factors(x, True)[1:-1]


def is_prime(x):
    return len(factors(x)) == 2
