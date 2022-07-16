"""
D - Circumferences
https://atcoder.jp/contests/abc259/tasks/abc259_d
"""

from itertools import combinations, product


N = int(input())
sx, sy, tx, ty = map(int, input().split())
points = [list(map(int, input().split())) for _ in range(N)]


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


uf = UnionFindTree(N)
start_circle = []
end_circle = []

for i in range(N):
    x, y, r = points[i]
    if (x - sx) ** 2 + (y - sy) ** 2 == r**2:
        start_circle.append(i)
    if (x - tx) ** 2 + (y - ty) ** 2 == r**2:
        end_circle.append(i)

for i, j in combinations(range(N), r=2):
    x1, y1, r1 = points[i]
    x2, y2, r2 = points[j]

    d2 = (x1 - x2) ** 2 + (y1 - y2) ** 2
    if (r1 - r2) ** 2 <= d2 <= (r1 + r2) ** 2:
        uf.union(i, j)

for start, end in product(start_circle, end_circle):
    if uf.same_check(start, end):
        print("Yes")
        exit()

print("No")
