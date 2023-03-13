"""
D - Tying Rope
https://atcoder.jp/contests/abc293/tasks/abc293_d
"""
from collections import defaultdict


class UnionFindTree:
    def __init__(self, n):
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.find(self.parents[x])

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.parents[x] > self.parents[y]:
            x, y = y, x
        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def same_check(self, x, y):
        return self.find(x) == self.find(y)

    def size(self, x):
        return -1 * self.parents[self.find(x)]


N, M = map(int, input().split())
uf = UnionFindTree(2 * N)
edges = []
for v in range(0, 2 * N, 2):
    uf.union(v, v + 1)
    edges.append((v, v + 1))

# R: 0, B: 1
for _ in range(M):
    q = list(input().split())
    a, b, c, d = int(q[0]), str(q[1]), int(q[2]), str(q[3])

    a = 2 * (a - 1)
    c = 2 * (c - 1)

    if b == "B":
        a += 1
    if d == "B":
        c += 1

    uf.union(a, c)
    edges.append((a, c))


connected_components_vertex = defaultdict(int)
for v in range(2 * N):
    root = uf.find(v)
    connected_components_vertex[root] += 1

connected_components_edges = defaultdict(int)
for u, v in edges:
    root = uf.find(u)
    connected_components_edges[root] += 1

num_tree = 0
for key in connected_components_vertex:
    num_vertex = connected_components_vertex[key]
    num_edges = connected_components_edges[key]

    if num_edges == num_vertex - 1:
        num_tree += 1


print(len(connected_components_vertex) - num_tree, num_tree)
