"""
E - Red Polyomino
https://atcoder.jp/contests/abc211/tasks/abc211_e
"""
from itertools import product
from collections import deque


def popcount(x):
    """xの立っているビット数をカウントする関数
    (xは64bit整数)"""

    # 2bitごとの組に分け、立っているビット数を2bitで表現する
    x = x - ((x >> 1) & 0x5555555555555555)

    # 4bit整数に 上位2bit + 下位2bit を計算した値を入れる
    x = (x & 0x3333333333333333) + ((x >> 2) & 0x3333333333333333)

    x = (x + (x >> 4)) & 0x0F0F0F0F0F0F0F0F  # 8bitごと
    x = x + (x >> 8)  # 16bitごと
    x = x + (x >> 16)  # 32bitごと
    x = x + (x >> 32)  # 64bitごと = 全部の合計
    return x & 0x0000007F


N = int(input())
K = int(input())
grid = [input() for _ in range(N)]

dq = deque()
for i, j in product(range(N), range(N)):
    if grid[i][j] == ".":
        dq.append((1 << (i * N + j), i, j))

ans = set()
appear = set()
while dq:
    (now, i, j) = dq.popleft()
    if popcount(now) == K:
        ans.add(now)
        continue

    for di, dj in zip([1, 0, -1, 0], [0, 1, 0, -1]):
        ni, nj = i + di, j + dj
        if not (0 <= ni < N and 0 <= nj < N):  # マスからはみ出したら
            continue
        if grid[ni][nj] == "#":  # 黒く塗られたマスなら
            continue
        if (now | 1 << (ni * N + nj), ni, nj) in appear:  # 既に現れた状態なら
            continue
        dq.append([now | 1 << (ni * N + nj), ni, nj])
        appear.add((now | 1 << (ni * N + nj), ni, nj))

print(len(ans))
