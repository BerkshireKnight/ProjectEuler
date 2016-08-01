#1/usr/bin/env python3

from euler18 import NumberTriangle, longest_path


def euler67():
    tri = NumberTriangle('triangle2.txt')
    dist, prev = longest_path(tri, tri.root)

    print(sorted(dist.values(), reverse=True)[0])


if __name__ == '__main__':
    euler67()
