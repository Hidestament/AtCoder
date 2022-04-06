"""
C - Collision 2
問題リンク: https://atcoder.jp/contests/abc243/tasks/abc243_c
"""

from collections import defaultdict


N = int(input())
points = [list(map(int, input().split())) for _ in range(N)]
S = str(input())

# y座標が同じ人たちでまとめる
pos = defaultdict(list)
for i in range(N):
    x, y = points[i]
    pos[y].append([x, i])

# 右を向いている人の右側に, 左を向いている人がいたら, 衝突する
flag = False
for y in pos:
    pos[y] = sorted(pos[y])
    tmp = False
    for x, i in pos[y]:
        direction = S[i]
        if (tmp) and (direction == "L"):
            flag = True

        if direction == "R":
            tmp = True

print("Yes" if flag else "No")
