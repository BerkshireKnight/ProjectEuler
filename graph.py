
import queue as q
from random import randint


MAX_UID = 0xffff


class Vertex:

    def __init__(self, uid, value):
        self.uid = uid
        self.value = value

    def __hash__(self):
        return self.uid

    def __eq__(self, other):
        return self.uid == other.uid


class Graph:

    def __init__(self):
        self.used_ids = set()
        self.vertices = set()
        self.edges = {}

    def add_vertex(self, value):
        v = Vertex(None, value)
        while True:
            v.uid = randint(0, MAX_UID)
            if not v.uid in self.used_ids:
                break

        self.vertices.add(v)
        self.edges[v] = {}
        return v

    def add_edge(self, v1, v2, w=None):
        self.edges[v1][v2] = w

    def get_neighbours(self, v):
        return self.edges[v].keys()


def longest_path(g, v0):
    dist, prev = {}, {}
    dist[v0] = 0

    query_set = q.PriorityQueue()
    query_set.put((v, 0))

    for v in g.vertices:
        if v != v0:
            dist[v] = -1
            prev[v] = None

    while not query_set.empty():
        u = query_set.get()        
        for v in g.get_neighbours(u):
            alt = dist[u] + v.value
            if alt > dist[v]:
                dist[v] = alt
                prev[v] = u
                query_set.put((1/alt, v))

    return dist, prev
