
import graph as g
import queue as q


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


def longest_path(G, v0):
    dist, prev = {}, {}
    dist[v0] = v0.value

    query_set = q.PriorityQueue()
    query_set.put((0, v))

    for v in G.vertices:
        if v != v0:
            dist[v] = -1
            prev[v] = None

    while not query_set.empty():
        (_, u) = query_set.get()        
        for v in G.get_neighbours(u):
            alt = dist[u] + v.value
            if alt > dist[v]:
                dist[v] = alt
                prev[v] = u
                query_set.put((1/alt, v))

    return dist, prev


def euler18():
    tri = NumberTriangle('triangle1.txt')
    dist, prev = longest_path(tri, tri.root)
