"""
D - LRUD Instructions
https://atcoder.jp/contests/abc273/tasks/abc273_d
"""
import sys
from collections import defaultdict
from bisect import bisect

input = sys.stdin.readline


H, W, rs, cs = map(int, input().split())
N = int(input())

walls_H = defaultdict(list)
walls_W = defaultdict(list)
for _ in range(N):
    r, c = map(int, input().split())
    walls_H[r].append(c)
    walls_W[c].append(r)

# sort & 番兵の追加
for key, value in walls_H.items():
    walls_H[key] = sorted([0] + value + [W + 1])

for key, value in walls_W.items():
    walls_W[key] = sorted([0] + value + [H + 1])


Q = int(input())

now_r, now_c = rs, cs
for _ in range(Q):
    q = list(input().split())
    to, length = q[0], int(q[1])

    if to == "L":
        # その列に壁が無い場合
        if walls_H[now_r] == []:
            walls_H[now_r] = [0, W + 1]

        left_wall_ind = bisect(walls_H[now_r], now_c) - 1
        left_wall = walls_H[now_r][left_wall_ind]
        now_c = max(now_c - length, left_wall + 1)

    elif to == "R":
        if walls_H[now_r] == []:
            walls_H[now_r] = [0, W + 1]

        right_wall_ind = bisect(walls_H[now_r], now_c)
        right_wall = walls_H[now_r][right_wall_ind]
        now_c = min(now_c + length, right_wall - 1)

    elif to == "U":
        if walls_W[now_c] == []:
            walls_W[now_c] = [0, H + 1]

        up_wall_ind = bisect(walls_W[now_c], now_r) - 1
        up_wall = walls_W[now_c][up_wall_ind]
        now_r = max(now_r - length, up_wall + 1)

    elif to == "D":
        if walls_W[now_c] == []:
            walls_W[now_c] = [0, H + 1]

        down_wall_ind = bisect(walls_W[now_c], now_r)
        down_wall = walls_W[now_c][down_wall_ind]
        now_r = min(now_r + length, down_wall - 1)

    print(now_r, now_c)
