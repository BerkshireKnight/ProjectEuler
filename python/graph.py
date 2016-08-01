
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

