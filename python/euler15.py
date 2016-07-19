#!/usr/bin/env python3


def euler15(n):
    paths = [[0 for _ in range(n+1)] for _ in range(n+1)]

    for i in range(0, n+1):
        for j in range(0, n+1):
            if i == 0 or j == 0:
                paths[i][j] = 1
            else:
                paths[i][j] = paths[i-1][j] + paths[i][j-1]

    return paths[n][n]


if __name__ == '__main__':
    import sys

    n = 20 if len(sys.argv) <= 1 else int(sys.argv[1])
    result = euler15(n)
    print(result)
