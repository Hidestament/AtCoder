"""
E - Graph Destruction
https://atcoder.jp/contests/abc229/tasks/abc229_e
UnionFindで管理しながら, 処理を逆順で行う
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
edges = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    a, b = min(a-1, b-1), max(a-1, b-1)
    edges[a].append(b)

uf = UnionFindTree(N)
num_cc = 0
ans = []
for i in range(N)[::-1]:
    ans.append(num_cc)
    num_cc += 1
    for to in edges[i]:
        if not uf.same_check(i, to):
            num_cc -= 1
            uf.union(i, to)

print(*ans[::-1], sep="\n")
