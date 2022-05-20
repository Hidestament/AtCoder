"""
E - Stronger Takahashi
https://atcoder.jp/contests/abc213/tasks/abc213_e
"""
from collections import deque
from itertools import product

H, W = map(int, input().split())
grid = [input() for _ in range(H)]
INF = 10**9

dq = deque()
dist = [[INF] * W for _ in range(H)]
dist[0][0] = 0
dq.append([0, 0])
while dq:
    h, w = dq.popleft()
    # コスト0の移動
    for dh, dw in zip([1, 0, -1, 0], [0, 1, 0, -1]):
        nh, nw = h + dh, w + dw
        if not (0 <= nh < H and 0 <= nw < W):
            continue

        if grid[nh][nw] == "#":
            continue

        if dist[nh][nw] > dist[h][w]:
            dist[nh][nw] = dist[h][w]
            dq.appendleft([nh, nw])

    # コスト1の移動
    for dh, dw in product(range(-3, 3), range(-3, 3)):
        nh, nw = h + dh, w + dw
        if not (0 <= nh < H and 0 <= nw < W):
            continue

        if abs(h - nh) + abs(w - nw) > 3:
            continue

        if dist[nh][nw] > dist[h][w] + 1:
            dist[nh][nw] = dist[h][w] + 1
            dq.append([nh, nw])

print(dist[H - 1][W - 1])
