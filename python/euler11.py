#!/usr/bin/env python

def get_grid():
    with open('grid.txt', 'r') as f:
        grid = [[int(n) for n in row] for
                 row in [l.split(' ')
                         for l in f.readlines()
                         ]
               ]

    return grid


def reverse(list):
    newlist = [0 for i in range(len(list))]
    for i in range(1, len(list)+1):
        newlist[i*-1] = list[i-1]

    return newlist


def horizontal_max(grid):
    maxval = 0
    for row in grid:
        for i in range(17):
            product = row[i]*row[i+1]*row[i+2]*row[i+3]
            maxval = product if product > maxval else maxval
    for row in grid:
        row = reverse(row)
        for i in range(17):
            product = row[i]*row[i+1]*row[i+2]*row[i+3]
            maxval = product if product > maxval else maxval

    return maxval


def vertical_max(grid):
    maxval = 0
    for i in range(20):
        for j in range(17):
            product = grid[j][i]*grid[j+1][i]*grid[j+2][i]*grid[j+3][i]
            maxval = product if product > maxval else maxval
    grid = [reverse(row) for row in grid]
    for i in range(20):
        for j in range(17):
            product = grid[j][i]*grid[j+1][i]*grid[j+2][i]*grid[j+3][i]
            maxval = product if product > maxval else maxval

    return maxval


def diagonal_max(grid):
    maxval = 0
    for i in range(17):
        for j in range(17):
            product = grid[i][j]*grid[i+1][j+1]*grid[i+2][j+2]*grid[i+3][j+3]
            maxval = product if product > maxval else maxval
    grid = [reverse(row) for row in grid]
    for i in range(17):
        for j in range(17):
            product = grid[i][j]*grid[i+1][j+1]*grid[i+2][j+2]*grid[i+3][j+3]
            maxval = product if product > maxval else maxval

    return maxval


def main():
    grid = get_grid()
    print max([horizontal_max(grid), vertical_max(grid), diagonal_max(grid)])


if __name__ == "__main__":
    main()
