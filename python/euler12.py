#!/usr/bin/env python3

from functools import reduce
from itertools import chain
from math import sqrt


def factors(n):
    factor_pairs = [(k, n//k) for k in range(1, int(sqrt(n))+1) if n % k == 0]
    factors = list(chain(*factor_pairs))
    return sorted(factors)


def triangle(n):
    return (n * (n+1)) / 2


def solution(n):
    k = 1
    while True:
        if len(factors(triangle(k))) >= n:
            return triangle(k)

        k += 1


if __name__ == "__main__":
    import sys

    n = int(sys.argv[1])
    print(solution(n))
