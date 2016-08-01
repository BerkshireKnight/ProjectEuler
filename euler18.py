
import graph as g


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

        self.root = grid[0][0]

        # create edges
        r, c = 0, 0
        while r < len(grid)-1:
            while c <= r:
                grid.add_edge(grid[r][c], grid[r+1][c])
                grid.add_edge(grid[r][c], grid[r+1][c+1])
                c += 1

            r += 1
