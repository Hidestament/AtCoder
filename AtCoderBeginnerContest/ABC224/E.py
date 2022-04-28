"""
E - Integers on Grid
https://atcoder.jp/contests/abc224/tasks/abc224_e
1. aが大きい順に処理する
2. 同じ行 or 列 の中で最大のものを高速に取得する
"""

from collections import defaultdict

H, W, N = map(int, input().split())
points = defaultdict(list)
for i in range(N):
    r, c, a = map(int, input().split())
    points[a].append([i, r, c])

dist_row = defaultdict(int)
dist_col = defaultdict(int)
ans = [None] * N
for a in sorted(points.keys(), reverse=True):
    same_value = []
    for i, r, c in points[a]:
        if (r not in dist_row) and (c not in dist_col):
            d = 0
        elif r not in dist_row:
            d = dist_col[c] + 1
        elif c not in dist_col:
            d = dist_row[r] + 1
        else:
            d = max(dist_row[r], dist_col[c]) + 1
        ans[i] = d
        same_value.append([r, c, d])

    for r, c, d in same_value:
        dist_row[r] = max(dist_row[r], d)
        dist_col[c] = max(dist_col[c], d)

print(*ans, sep="\n")
