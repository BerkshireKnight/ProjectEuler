#!/usr/bin/env python3

from itertools import chain
from math import sqrt
from utils.factors import factors


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
