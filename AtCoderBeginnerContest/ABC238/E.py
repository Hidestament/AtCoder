"""
E - Range Sums
https://atcoder.jp/contests/abc238/tasks/abc238_e
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


N, Q = map(int, input().split())
uf = UnionFindTree(N+1)
for _ in range(Q):
    l, r = map(int, input().split())
    uf.union(l-1, r)

print("Yes" if uf.same_check(0, N) else "No")
