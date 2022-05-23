"""
E - Road Reduction
https://atcoder.jp/contests/abc252/tasks/abc252_e
最短経路木を求めれば良い
"""
from heapq import heappush, heappop

N, M = map(int, input().split())
graph = [[] for _ in range(N)]
for e in range(M):
    a, b, c = map(int, input().split())
    graph[a - 1].append([b - 1, c, e])
    graph[b - 1].append([a - 1, c, e])

INF = 10**15
dist = [INF] * N
flag = [0] * N
dist[0] = 0
hq = [[0, 0, -1]]
ans = []
while hq:
    _, now, num_edge = heappop(hq)
    if flag[now]:
        continue
    flag[now] = 1
    ans.append(num_edge + 1)

    for to, cost, e in graph[now]:
        if flag[to]:
            continue
        if dist[to] < dist[now] + cost:
            continue
        dist[to] = dist[now] + cost
        heappush(hq, [dist[to], to, e])

print(*ans[1:])
