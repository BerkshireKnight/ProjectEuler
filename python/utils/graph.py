
import utils.priority_queue as pq
from random import randint
import sys


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
        if self.value is not None and other.value is not None:
            return self.value, self.uid < other.value, other.uid
        else:
            return self.uid < other.uid

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

        self.used_ids.add(v.uid)
        self.vertices.add(v)
        self.edges[v] = {}
        return v

    def add_edge(self, v1, v2, w):
        self.edges[v1][v2] = w


    def get_edge(self, v1, v2):
        return self.edges[v1][v2]

    def get_neighbours(self, v):
        return self.edges[v].keys()


def shortest_path(graph, source, shortest=True):
    """Uses Dijkstra's algorithm to compute the shortest paths from the source
    to all other vertices reachable from the source.

    Optionally, may be used to find the longest route instead.
    """
    dist, prev = {}, {}
    dist[source] = 0
    prev[source] = None

    query_set = pq.PriorityQueue()
    query_set.push(source, 0)

    for v in graph.vertices:
        if v != source:
            dist[v] = sys.maxsize if shortest else -sys.maxsize
            prev[v] = None

    while not query_set.empty():
        u = query_set.pop()
        for v in graph.get_neighbours(u):
            alt = dist[u] + graph.get_edge(u, v)
            if (shortest and alt < dist[v]) or alt > dist[v]:
                dist[v] = alt
                prev[v] = u
                query_set.push(v, alt if shortest else -alt)

    return dist, prev
