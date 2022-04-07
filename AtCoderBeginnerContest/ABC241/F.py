"""
F - Skate
https://atcoder.jp/contests/abc241/tasks/abc241_f
ブロックの４方にしか到達できない
-> 4 * ブロックの個数のマスにしかいけない
-> 実質 |V| = 4*N, |E| = 4*N 程度のグラフになる
-> うまくBFSをやれば解ける
"""

from collections import deque, defaultdict
from bisect import bisect_left


H, W, N = map(int, input().split())
sx, sy = map(int, input().split())
gx, gy = map(int, input().split())

# ブロックの場所を, x軸, y軸ベースで持っておく
block_x = defaultdict(list)
block_y = defaultdict(list)
for _ in range(N):
    x, y = map(int, input().split())
    block_x[x].append(y)
    block_y[y].append(x)

# 二分探索で一番近いブロックを探すので, ソートする
for x in block_x:
    block_x[x] = sorted(block_x[x])
for y in block_y:
    block_y[y] = sorted(block_y[y])


dq = deque()
INF = 10**10
dist = defaultdict(lambda: INF)

dist[(sx, sy)] = 0
dq.append([sx, sy])

while dq:
    x, y = dq.popleft()
    if (x == gx) and (y == gy):
        break

    # 右へ移動: xが同じ, yが大きく
    ind = bisect_left(block_x[x], y)
    if ind < len(block_x[x]):
        nx, ny = x, block_x[x][ind] - 1
        if dist[x, y] + 1 < dist[nx, ny]:
            dist[nx, ny] = dist[x, y] + 1
            dq.append([nx, ny])

    # 左へ移動: xが同じ, yが小さく
    ind = bisect_left(block_x[x], y)
    if 0 <= ind - 1:
        nx, ny = x, block_x[x][ind-1] + 1
        if dist[x, y] + 1 < dist[nx, ny]:
            dist[nx, ny] = dist[x, y] + 1
            dq.append([nx, ny])

    # 下へ移動: yが同じ, xが大きく
    ind = bisect_left(block_y[y], x)
    if ind < len(block_y[y]):
        nx, ny = block_y[y][ind] - 1, y
        if dist[x, y] + 1 < dist[nx, ny]:
            dist[nx, ny] = dist[x, y] + 1
            dq.append([nx, ny])

    # 上へ移動: yが同じ, xが小さく
    ind = bisect_left(block_y[y], x)
    if 0 <= ind - 1:
        nx, ny = block_y[y][ind-1] + 1, y
        if dist[x, y] + 1 < dist[nx, ny]:
            dist[nx, ny] = dist[x, y] + 1
            dq.append([nx, ny])

print(dist[gx, gy] if dist[gx, gy] < INF else -1)
