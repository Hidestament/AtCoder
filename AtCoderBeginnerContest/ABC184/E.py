"""
E - Third Avenue
https://atcoder.jp/contests/abc184/tasks/abc184_e
"""


from collections import defaultdict, deque
from itertools import product


H, W = map(int, input().split())
grid = ["#" * (W + 2)]
for _ in range(H):
    a = "#" + input() + "#"
    grid.append(a)
grid.append("#" * (W + 2))

H += 2
W += 2

teleporter = defaultdict(list)
for h, w in product(range(H), range(W)):
    if grid[h][w] == ".":
        continue
    elif grid[h][w] == "#":
        continue
    elif grid[h][w] == "S":
        sh, sw = h, w
    elif grid[h][w] == "G":
        gh, gw = h, w
    else:
        teleporter[grid[h][w]].append((h, w))

dist = [[-1] * W for _ in range(H)]
used_teleporter = set()
dist[sh][sw] = 0
dq = deque([[sh, sw]])
while dq:
    h, w = dq.popleft()
    if (h, w) == (gh, gw):
        break

    # 隣接マスへの移動
    for dh, dw in zip([1, 0, -1, 0], [0, 1, 0, -1]):
        nh, nw = h + dh, w + dw
        if grid[nh][nw] == "#":
            continue
        if dist[nh][nw] != -1:
            continue
        dist[nh][nw] = dist[h][w] + 1
        dq.append([nh, nw])

    # テレポート
    if ord("a") <= ord(grid[h][w]) <= ord("z"):
        if grid[h][w] not in used_teleporter:
            used_teleporter.add(grid[h][w])
            for nh, nw in teleporter[grid[h][w]]:
                if dist[nh][nw] != -1:
                    continue
                dist[nh][nw] = dist[h][w] + 1
                dq.append([nh, nw])

print(dist[gh][gw])
