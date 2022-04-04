"""枝刈りBFSで行う
"""


from collections import deque


N = int(input())
Ax, Ay = map(int, input().split())
Bx, By = map(int, input().split())

# 番兵を入れる
grid = ["#" * (N + 2)]
for _ in range(N):
    s = input()
    grid.append("#" + s + "#")
grid.append("#" * (N + 2))

INF = 10**9
dist = [[INF] * (N+2) for _ in range(N+2)]
dist[Ax][Ay] = 0
dq = deque()
dq.append([Ax, Ay])

move = [[1, 1], [-1, 1], [1, -1], [-1, -1]]
while dq:
    x, y = dq.popleft()

    for t in range(4):
        dx, dy = move[t]
        for d in range(1, N+2):
            nx, ny = x + d*dx, y + d*dy
            # 壁に行き当たったら終了
            if grid[nx][ny] == "#":
                break
            # 既にコストが低い更新があったなら, 終了
            if dist[nx][ny] < dist[x][y] + 1:
                break
            if dist[nx][ny] > dist[x][y] + 1:
                dist[nx][ny] = dist[x][y] + 1
                dq.append([nx, ny])

print(dist[Bx][By] if dist[Bx][By] < INF else -1)
