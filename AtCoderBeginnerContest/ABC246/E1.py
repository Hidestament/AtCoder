"""
E - Bishop
問題リンク: https://atcoder.jp/contests/abc246/tasks/abc246_e
0-1BFSで解く
"""

from collections import deque


N = int(input())
Ax, Ay = map(int, input().split())
Bx, By = map(int, input().split())
grid = [input() for _ in range(N)]

Ax, Ay = Ax-1, Ay-1
Bx, By = Bx-1, By-1

INF = 10**9
dist = [[[INF] * 4 for _ in range(N)] for _ in range(N)]
dq = deque()
move = [[1, 1], [1, -1], [-1, 1], [-1, -1]]

for t in range(4):
    dx, dy = move[t]
    nx, ny = Ax + dx, Ay + dy

    if not (0 <= nx < N and 0 <= ny < N):
        continue
    if grid[nx][ny] == "#":
        continue
    dist[nx][ny][t] = 1
    dq.append([nx, ny, t])

while dq:
    x, y, direction = dq.popleft()
    if (x == Bx) and (y == By):
        break

    for t in range(4):
        dx, dy = move[t]
        nx, ny = x + dx, y + dy
        if not (0 <= nx < N and 0 <= ny < N):
            continue
        if grid[nx][ny] == "#":
            continue

        if t == direction:
            if dist[nx][ny][t] > dist[x][y][t]:
                dist[nx][ny][t] = dist[x][y][t]
                dq.appendleft([nx, ny, t])
        else:
            if dist[nx][ny][t] > dist[x][y][direction] + 1:
                dist[nx][ny][t] = dist[x][y][direction] + 1
                dq.append([nx, ny, t])

print(min(dist[Bx][By]) if min(dist[Bx][By]) < INF else - 1)
