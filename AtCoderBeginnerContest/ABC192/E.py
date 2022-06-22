"""
E - Train
https://atcoder.jp/contests/abc192/tasks/abc192_e
"""
from heapq import heappush, heappop

N, M, X, Y = map(int, input().split())
X -= 1
Y -= 1

graph = [[] for _ in range(N)]
for _ in range(M):
    a, b, t, k = map(int, input().split())
    graph[a - 1].append((b - 1, t, k))
    graph[b - 1].append((a - 1, t, k))

INF = 10**15
dist = [INF] * N
flag = [0] * N
dist[X] = 0
hq = [[0, X]]

while hq:
    d, now = heappop(hq)

    if now == Y:
        break

    if flag[now]:
        continue

    flag[now] = 1

    for to, t, k in graph[now]:
        to_time = -int(-d // k) * k
        arrive_time = to_time + t
        if arrive_time < dist[to]:
            dist[to] = arrive_time
            heappush(hq, [dist[to], to])

print(dist[Y] if dist[Y] < INF else -1)
