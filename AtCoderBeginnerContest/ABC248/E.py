"""
E - K-colinear Line
https://atcoder.jp/contests/abc248/tasks/abc248_e
"""

from itertools import combinations


N, K = map(int, input().split())
points = [list(map(int, input().split())) for _ in range(N)]

if N == 1 or K == 1:
    print("Infinity")
    exit()


def check(x1, y1, x2, y2, x, y):
    if (x2 - x1) * (y - y1) == (y2 - y1) * (x - x1):
        return True
    else:
        return False


# まずは直線を計算する
ans = set()
for i, j in combinations(range(N), r=2):
    x1, y1 = points[i]
    x2, y2 = points[j]
    cnt = [i, j]
    for k in range(N):
        if (k == i) or (k == j):
            continue
        x, y = points[k]
        if check(x1, y1, x2, y2, x, y):
            cnt.append(k)
    cnt = tuple(sorted(cnt))
    if len(cnt) >= K:
        ans.add(cnt)

print(len(ans))
