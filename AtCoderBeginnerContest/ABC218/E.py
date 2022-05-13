"""
E - Destruction
https://atcoder.jp/contests/abc218/tasks/abc218_e
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


N, M = map(int, input().split())
uf = UnionFindTree(N)
positive_edges = []
for _ in range(M):
    a, b, c = map(int, input().split())
    if c <= 0:
        uf.union(a - 1, b - 1)
    else:
        positive_edges.append([c, a - 1, b - 1])

positive_edges.sort()
ans = 0
for c, a, b in positive_edges:
    if not uf.same_check(a, b):
        uf.union(a, b)
    else:
        ans += c

print(ans)
