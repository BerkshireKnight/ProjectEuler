#!/usr/bin/env python

def num_factors(n):
    return len([x for x in range(1,n+1) if n%x == 0])


def triangle_sum(n):
    return sum([x for x in range(n+1)])


def thousands_bound():
    lower = 1000
    upper = 2000
    while num_factors(triangle_sum(upper)) <= 500:
        lower += 1000
        upper += 1000

    return lower


def hundreds_bound(lower_bound):
    lower = lower_bound
    upper = lower + 100
    while num_factors(triangle_sum(upper)) <= 500:
        lower += 100
        upper += 100

    return lower


def tens_bound(lower_bound):
    lower = lower_bound
    upper = lower + 10
    while num_factors(triangle_sum(upper)) <= 500:
        lower += 10
        upper += 10

    return lower


def solve_problem(lower_bound):
    value = lower_bound
    while num_factors(triangle_sum(upper)) <= 500:
        value += 1

    return value


def main():
    b1 = thousands_bound()
    b2 = hundreds_bound(b1)
    b3 = tens_bound(b2)
    print b1, b2, b3
    # print "The first triangle number with over 500 factors is {}.".format(
    #     solve_problem(tens_bound(hundreds_bound(thousands_bound())))
    #     )


if __name__ == "__main__":
    main()
