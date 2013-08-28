#!/usr/bin/env python

def factors(x):
    return [n for n in range(1,x) if x%n == 0]


def are_amicable(x, y):
    return (sum(factors(x)) == y) and (sum(factors(y)) == x)


def main():
    pairs = [sum((n,m)) for n in range(1,10000)
                        for m in range(n+1,10000)
                        if are_amicable(n,m)
                        ]

    print "There are {} pairs:".format(len(pairs))
    for p in pairs:
        print p


if __name__ == "__main__":
    main()
