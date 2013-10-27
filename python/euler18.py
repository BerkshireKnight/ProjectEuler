#!/usr/bin/env python

from random import choice, randint, random
from math import exp
from sys import argv


def read_grid(filename):
    """
    Reads the triangle of numbers described in 'filename' into a list
    of lists.

    """

    grid = []
    with open(filename, "r") as grid_file:
        for line in grid_file:
            grid.append([int(n) for n in line.split(" ")])

    return grid


def grid_max_cost(grid):
    """Calculates the maximum possible path cost in the given grid."""
    return len(grid) * 99


def get_random_move(grid, start_row, start_index):
    """
    Generates a random move from position grid[start_row][start_index].

    Returns a singleton list containing the index of the element that should
    be chosen after grid[start_row][start_index], or the empty list if the
    last row has been reached.

    """

    return [] if start_row == len(grid)-1 else [
        choice([start_index,start_index+1])
        ]


def get_random_path(base_path, grid):
    """
    Generates a random path from the top of the grid to the bottom.

    A path is a list of integers, representing the indicies of the elements
    to be chosen from each row, in order. That is, in the path [0,1,2], we
    should choose element 0 in row 0, element 1 in row 1, and element 2 in
    row 2.

    """

    path = base_path if len(base_path) > 0 else [0]
    for row_num in range(len(base_path)-1, len(grid)):
        path += get_random_move(grid, row_num, path[-1])

    return path


def path_cost(path, grid):
    """Calculates the cost of the given path through the grid."""

    return sum([grid[i][path[i]] for i in range(len(grid))])


def path_heuristic(path, grid):
    """
    Calculates the optimality of the given path. The heuristic of a path is
    equal to the maximum path cost in the grid, minus the cost of the
    given path.

    """

    return grid_max_cost(grid) - path_cost(path, grid)


def get_random_successors(n, path, grid):
    """
    Returns n paths which have at least some steps in common with the given
    path. Achieved by retaining a random number of steps from the base
    path, and then randomly generating a new path from that root.

    Each successor is guaranteed to retain at least a quarter of the original
    path, and to retain no more than three quarters of the original path.

    """

    successors = []
    for i in range(n):
        divider = randint(len(grid)//4, (len(grid)*3)//4)
        while True:
            s = get_random_path(path[:divider], grid)
            if s != path:
                break
        successors.append(s)

    return successors


def anneal(path, grid, T):
    """
    Generates a new path through the grid, based on the given path.

    The algorithm generates a number of random successors from the given path,
    and selects the best one. If it is better than the given path, it is
    returned. If not, then it may be returned anyway, with a probability equal
    to a function of its heuristic function and the current 'temperature'.

    """

    # generate a random list of successors, calculate their heuristics, and
    # identify the best successor
    successors = get_random_successors(5, path, grid)
    heuristics = [path_heuristic(s, grid) for s in successors]
    candidate = successors[heuristics.index(max(heuristics))]

    # calculate the 'energy change' resulting from moving from the current
    # path to the candidate, and determine whether to return the candidate
    # or the original path
    energy_change = (-1) * (
        path_heuristic(path, grid) -
        path_heuristic(candidate, grid)
        )
    if energy_change < 0:
        # candidate has lower energy
        return candidate
    else:
        # candidate has higher energy
        try:
            p = exp(-energy_change / T)
            return candidate if random() <= p else path
        except OverflowError:
            print("Energy change = %d" % energy_change)
            print("Temperature = %f" % T)
            print("Overflow error, quitting")
            exit(2)


def euler18(num_tries=500):
    """The main method for the solution."""

    # read in the grid, and determine the best sample size
    grid = read_grid("numbers-euler18.txt")
    sample_size = len(grid)//3

    # run the annealing algorithm on 'num_tries' different samples
    solutions = []
    for i in range(num_tries):
        # get an initial sample and set the starting temperature
        sample = [get_random_path([], grid) for i in range(sample_size)]
        T = 100
        # successively generate successors until the temperature reaches 0
        while T > 0:
            sample = [anneal(s, grid, T) for s in sample]
            T -= 0.1
        # add the best solution in the sample to the list of solutions
        heuristics = [path_heuristic(s, grid) for s in sample]
        solutions.append(sample[heuristics.index(max(heuristics))])

    # determine the best solution found
    costs = [path_cost(s, grid) for s in solutions]
    best_solution = solutions[costs.index(max(costs))]
    # display solution
    print([grid[i][best_solution[i]] for i in range(len(grid))])
    print(path_cost(best_solution, grid))
    exit(0)


if __name__ == "__main__":
    if len(argv) > 1:
        try:
            euler18(int(argv[1]))
        except ValueError:
            print("Failed to set tries from command line, defaulting to 500")
            euler18()
    else:
        euler18()
