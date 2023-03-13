"""
D - Takahashi's Solitaire
https://atcoder.jp/contests/abc277/tasks/abc277_d
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
A = sorted(list(map(int, input().split())))

uf = UnionFindTree(N)
for i, j in zip(range(N), range(1, N)):
    if (A[i] == A[j]) or (A[i] + 1 == A[j]):
        uf.union(i, j)

if (A[0] == A[-1]) or (A[0] == (A[-1] + 1) % M):
    uf.union(0, N - 1)


connected_components = defaultdict(list)
for v in range(N):
    connected_components[uf.find(v)].append(v)

ans = float("inf")
total = sum(A)
for key, value in connected_components.items():
    s = sum(A[i] for i in value)
    ans = min(ans, total - s)

print(ans)
