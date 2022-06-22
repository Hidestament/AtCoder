"""
E - Come Back Quickly
https://atcoder.jp/contests/abc191/tasks/abc191_e
"""
from heapq import heappush, heappop

INF = 10**15

N, M = map(int, input().split())
graph = [[] for _ in range(N)]
loop = [INF] * N
for _ in range(M):
    a, b, c = map(int, input().split())
    if a == b:
        loop[a - 1] = min(loop[a - 1], c)
    else:
        graph[a - 1].append((b - 1, c))


def dijkstra(s):
    dist = [INF] * N
    flag = [0] * N
    hq = []

    for to, cost in graph[s]:
        dist[to] = cost
        heappush(hq, [dist[to], to])

    while hq:
        d, now = heappop(hq)

        if now == s:
            break

        if flag[now]:
            continue

        flag[now] = 1
        for to, cost in graph[now]:
            if cost + d < dist[to]:
                dist[to] = cost + d
                heappush(hq, [dist[to], to])
    return dist[s]


for v in range(N):
    dist = min(loop[v], dijkstra(v))
    print(dist if dist < INF else -1)
