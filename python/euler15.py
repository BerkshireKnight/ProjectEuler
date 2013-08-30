#!/usr/bin/env python

def matrix_sum(matrix):
    return sum([sum(row) for row in matrix])


def construct_grid():
    grid = [[2 for i in range(21)] for j in range(21)]
    for i in range(21):
        grid[i][20] = 1
        grid[20][i] = 1

    grid[20][20] = 0

    return grid


def main():
    print matrix_sum(construct_grid())


if __name__ == "__main__":
    main()
