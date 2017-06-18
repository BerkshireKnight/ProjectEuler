#!/usr/bin/env python3

from utils.factors import factors


def abundant(n):
    return sum(factors(n)) > n


def euler23():
    ns = [n for n in range(12, 28124) if abundant(n)]

    i, j = 0, 0
    sums = set()
    while i < len(ns):
        while j < len(ns):
            sums.add(ns[i] + ns[j])
            j += 1

        i += 1
        j = i
