
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

    def __ne__(self, other):
        return not self == other


    def __lt__(self, other):
        return self.value, self.uid < other.value, other.uid

    def __gt__(self, other):
        return other < self

    def __le__(self, other):
        return not self > other

    def __ge__(self, other):
        return not self < other


    def __repr__(self):
        return "Vertex ({:04x}): {}".format(self.uid, self.value)

    def __str__(self):
        return str(self.value)


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

