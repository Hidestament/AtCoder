"""
F - Cards
https://atcoder.jp/contests/abc247/tasks/abc247_f
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
P = list(map(int, input().split()))
Q = list(map(int, input().split()))
MOD = 998244353

uf = UnionFindTree(N)
for p, q in zip(P, Q):
    uf.union(p-1, q-1)

F = [0] * (N + 10)
F[1], F[2] = 2, 3
for i in range(3, N+5):
    F[i] = F[i-1] + F[i-2]
    F[i] %= MOD

G = [0] * (N + 10)
G[1], G[2], G[3] = 1, 3, 4
for i in range(4, N+5):
    G[i] = F[i-1] + F[i-3]
    G[i] %= MOD

ans = 1
for i in range(N):
    if uf.parents[i] < 0:
        size = -1 * uf.parents[i]
        ans *= G[size]
        ans %= MOD

print(ans)
