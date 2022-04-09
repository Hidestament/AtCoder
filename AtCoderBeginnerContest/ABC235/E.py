"""
E - MST + 1
https://atcoder.jp/contests/abc235/tasks/abc235_e
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


N, M, Q = map(int, input().split())

edges = []
for _ in range(M):
    a, b, c = map(int, input().split())
    edges.append([c, a-1, b-1, -1])

for q in range(Q):
    a, b, c = map(int, input().split())
    edges.append([c, a-1, b-1, q])

edges.sort()

ans = ["No"] * Q
uf = UnionFindTree(10**6)
for c, a, b, q in edges:
    if not uf.same_check(a, b):
        if q != -1:
            ans[q] = "Yes"
        else:
            uf.union(a, b)

print(*ans)
