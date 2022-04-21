"""
D - Neighbors
https://atcoder.jp/contests/abc231/tasks/abc231_d
駄目条件
1. 閉路がある
2. 次数が3以上
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
degree = defaultdict(int)
uf = UnionFindTree(N + 10)
for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    degree[a] += 1
    degree[b] += 1
    if uf.same_check(a, b):
        print("No")
        exit()
    uf.union(a, b)

if degree:
    max_deg = max(degree.values())
    if max_deg >= 3:
        print("No")
        exit()

print("Yes")
