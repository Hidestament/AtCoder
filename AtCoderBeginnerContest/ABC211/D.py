"""
D - Number of Shortest paths
https://atcoder.jp/contests/abc211/tasks/abc211_d
"""
from collections import deque


N, M = map(int, input().split())
MOD = 10**9 + 7
graph = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)

INF = 10**9
dist = [INF] * N
dist[0] = 0

# DP[i]: iにたどり着く最短経路の個数
DP = [0] * N
DP[0] = 1

dq = deque([0])
while dq:
    now = dq.popleft()
    for to in graph[now]:
        if dist[to] == dist[now] + 1:
            DP[to] += DP[now]
            DP[to] %= MOD
        elif dist[to] > dist[now] + 1:
            dist[to] = dist[now] + 1
            DP[to] = DP[now]
            dq.append(to)

print(DP[-1])
