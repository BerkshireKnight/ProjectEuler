#!/usr/bin/env python

from math import sqrt


def factors(n):
    return set(reduce(list.__add__,
                ([i, n//i] for i in range(1, int(sqrt(n)) + 1) if n % i == 0))
    )


def triangle(n):
    return (n * (n+1)) / 2


def ten_thousands_bound():
    lower = 0
    upper = 10000
    while len(factors(triangle(upper))) <= 500:
        lower += 10000
        upper += 10000

    return lower


def thousands_bound(lower_bound):
    lower = lower_bound
    upper = lower + 1000
    while len(factors(triangle(upper))) <= 500:
        lower += 1000
        upper += 1000

    return lower


def hundreds_bound(lower_bound):
    lower = lower_bound
    upper = lower + 100
    while len(factors(triangle(upper))) <= 500:
        lower += 100
        upper += 100

    return lower


def tens_bound(lower_bound):
    lower = lower_bound
    upper = lower + 10
    while len(factors(triangle(upper))) <= 500:
        lower += 10
        upper += 10

    return lower


def solve_problem(lower_bound):
    value = lower_bound
    while len(factors(triangle(value))) <= 500:
        value += 1

    return triangle(value)


def main():
    print "n\t\tnth number\t\tnumber of factors"
    for i in range(1,101):
        print "{}\t\t{}\t\t{}".format(
            i,
            triangle(i),
            len(factors(triangle(i)))
            )


if __name__ == "__main__":
    main()
