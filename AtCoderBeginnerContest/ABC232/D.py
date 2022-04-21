"""
D - Weak Takahashi
https://atcoder.jp/contests/abc232/tasks/abc232_d
"""

from collections import deque


H, W = map(int, input().split())
grid = ["#" * (W + 2)]
for _ in range(H):
    c = str(input())
    grid.append("#" + c + "#")
grid.append("#" * (W + 2))


seen = [[0] * (W + 2) for _ in range(H + 2)]
seen[1][1] = 1
dq = deque([])
dq.append([1, 1, 1])
ans = 0

while dq:
    h, w, c = dq.popleft()
    for dh, dw in zip([1, 0], [0, 1]):
        nh, nw = h+dh, w+dw
        if grid[nh][nw] == "#":
            ans = max(ans, c)
            continue
        if seen[nh][nw] == 1:
            continue
        dq.append([nh, nw, c+1])
        seen[nh][nw] = 1

print(ans)
