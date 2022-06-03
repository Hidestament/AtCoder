"""
D - KAIBUNsyo
https://atcoder.jp/contests/abc206/tasks/abc206_d
"""


class UnionFindTree:
    def __init__(self, n=10**6):
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
A = list(map(int, input().split()))
uf = UnionFindTree()

rA = A[::-1]
for i in range(N):
    a, b = A[i], rA[i]
    uf.union(a, b)

ans = sum((-num_c - 1) for num_c in uf.parents if num_c < 0)
print(ans)
