"""
D - Sum of Maximum Weights
https://atcoder.jp/contests/abc214/tasks/abc214_d
"""


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


N = int(input())
edges = []
for _ in range(N - 1):
    u, v, w = map(int, input().split())
    edges.append((u - 1, v - 1, w))
edges.sort(key=lambda x: x[2])

cnt = 0
uf = UnionFindTree(N)
for u, v, w in edges:
    if uf.same_check(u, v):
        continue
    u_size = uf.size(u)
    v_size = uf.size(v)
    cnt += u_size * v_size * w
    uf.union(u, v)

print(cnt)
