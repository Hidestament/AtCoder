"""
C - Triangle?
https://atcoder.jp/contests/abc224/tasks/abc224_c
"""

from itertools import combinations


N = int(input())
points = [list(map(int, input().split())) for _ in range(N)]


def check(x, y, x1, y1, x2, y2):
    return (y - y1)*(x2 - x1) == (y2 - y1) * (x - x1)


ans = 0
for i, j, k in combinations(range(N), r=3):
    x, y = points[i]
    x1, y1 = points[j]
    x2, y2 = points[k]
    if not check(x, y, x1, y1, x2, y2):
        ans += 1

print(ans)
