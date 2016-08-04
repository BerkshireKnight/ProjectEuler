#1/usr/bin/env python3

from euler18 import NumberTriangle
import utils.graph as g


def euler67():
    tri = NumberTriangle('triangle2.txt')
    dist, prev = g.shortest_path(tri, tri.root, False)

    print(sorted(dist.values(), reverse=True)[0])


if __name__ == '__main__':
    euler67()
