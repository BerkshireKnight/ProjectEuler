#/usr/bin/env python3

import utils.graph as g


class NumberTriangle(g.Graph):
    """A specialised Graph for storing a triangle of numbers."""
    def __init__(self, filename):
        super(NumberTriangle, self).__init__()

        # create vertices
        grid = []
        with open(filename, 'r') as f:
            for line in f:
                row = []
                for num in line.split(' '):
                    row.append(self.add_vertex(int(num)))

                grid.append(row)

        self.root = self.add_vertex(None)
        self.add_edge(self.root, grid[0][0], grid[0][0].value)

        # create edges
        r, c = 0, 0
        while r < len(grid)-1:
            while c <= r:
                self.add_edge(grid[r][c], grid[r+1][c], grid[r+1][c].value)
                self.add_edge(grid[r][c], grid[r+1][c+1], grid[r+1][c+1].value)
                c += 1

            c = 0
            r += 1


def euler18():
    tri = NumberTriangle('triangle1.txt')
    dist, prev = g.shortest_path(tri, tri.root, False)

    print(sorted(dist.values(), reverse=True)[0])


if __name__ == '__main__':
    euler18()
