"""
E - Takahashi's Anguish
https://atcoder.jp/contests/abc256/tasks/abc256_e
参考: https://atcoder.jp/contests/abc256/editorial/4135
"""

N = int(input())
X = [0] + list(map(int, input().split()))
C = [0] + list(map(int, input().split()))


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


uf = UnionFindTree(10**6)
loop_start = []
for now, to in enumerate(X[1:], start=1):
    if uf.same_check(now, to):
        loop_start.append(now)
    uf.union(now, to)

ans = 0
for root in loop_start:
    now = root
    min_cycle = 10**15
    while True:
        to = X[now]
        min_cycle = min(min_cycle, C[now])
        if to == root:
            break
        now = to
    ans += min_cycle

print(ans)
