"""
E - K-colinear Line
https://atcoder.jp/contests/abc248/tasks/abc248_e
2頂点を通る直線が, 何個の頂点を通るかを計算 -> 答えをsetで管理して重複を省く
"""

from itertools import combinations


N, K = map(int, input().split())
points = [list(map(int, input().split())) for _ in range(N)]

if K == 1:
    print("Infinity")
    exit()


def check(x1, y1, x2, y2, x, y):
    """(x1, y1), (x2, y2)を通る直線が, (x, y)を通るか判定
    """
    if (x2 - x1) * (y - y1) == (y2 - y1) * (x - x1):
        return True
    else:
        return False


ans = set()
for i, j in combinations(range(N), r=2):  # 2頂点を通る直線
    x1, y1 = points[i]
    x2, y2 = points[j]
    cnt = [i, j]
    for k in range(N):  # 何個の点を通るか
        if (k == i) or (k == j):
            continue
        x, y = points[k]
        if check(x1, y1, x2, y2, x, y):
            cnt.append(k)

    cnt = tuple(sorted(cnt))
    if len(cnt) >= K:
        ans.add(cnt)

print(len(ans))
