#!/usr/bin/env python

from math import sqrt


def factors(n):
    return set(reduce(list.__add__,
                ([i, n//i] for i in range(1, int(sqrt(n)) + 1) if n % i == 0))
    )


def triangle(n):
    return (n * (n+1)) / 2


def solution(n):
    val = n
    while len(factors(triangle(val))) <= 500:
        n += 1

    return triangle(val)


def main():
    print solution(1)


if __name__ == "__main__":
    main()
