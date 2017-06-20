#!/usr/bin/env python3

from utils.factors import proper_factors


def get_abundant(n):

    def abundant(m):
        return sum(proper_factors(m)) > m

    return [n for n in range(n) if abundant(n)]


def euler23():
    ns, ms = get_abundant(28124), set()

    i, j = 0, 0
    while i < len(ns):
        while j < len(ns):
            ms.add(ns[i] + ns[j])
            j += 1

        i += 1
        j = i

    total = 0
    for k in range(28124):
        if k not in ms:
            total += k

    return k


if __name__ == '__main__':
    print(euler23())
