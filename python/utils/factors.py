
from math import sqrt

ALL = 0
PROPER = 1
NON_TRIVIAL = 2


def find_factors(x, t):
    results = set()
    for x1 in range(1, sqrt(x)+2):
        if t == NON_TRIVIAL and x1 == 1:
            continue
        elif t == PROPER and x1 == 1:
            results.add(x1)
        else:
            results.add(x1)
            results.add(x // x1)

    return results


def factors(x):
    return find_factors(x, ALL)


def proper_factors(x):
    return find_factors(x, PROPER)


def non_trivial_factors(x):
    return find_factors(x, NON_TRIVIAL)


def is_prime(x):
    return len(factors(x)) == 2
