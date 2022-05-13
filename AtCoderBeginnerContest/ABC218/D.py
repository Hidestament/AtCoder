"""
D - Rectangles
https://atcoder.jp/contests/abc218/tasks/abc218_d
"""
from itertools import combinations


N = int(input())
points = [list(map(int, input().split())) for _ in range(N)]
table = {(p[0], p[1]): i for i, p in enumerate(points)}

ans = set()
for i, j in combinations(range(N), r=2):
    ix, iy = points[i]
    jx, jy = points[j]

    left_up = (ix, jy)
    right_down = (jx, iy)
    if (left_up in table) and (right_down in table):
        s = set([i, j, table[left_up], table[right_down]])
        if len(s) == 4:
            ans.add(tuple(sorted(s)))

print(len(ans))
