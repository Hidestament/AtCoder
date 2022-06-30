"""
F - Teleporter Setting
https://atcoder.jp/contests/abc257/tasks/abc257_f
"""

from collections import deque


INF = 10**15
N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)


def dfs(start):
    dq = deque([start])
    dist = [INF] * (N + 1)
    dist[start] = 0
    while dq:
        now = dq.popleft()
        for to in graph[now]:
            if dist[to] < INF:
                continue
            dist[to] = dist[now] + 1
            dq.append(to)
    return dist


dist1 = dfs(1)
distN = dfs(N)

ans = []
for i in range(1, N + 1):
    directed = dist1[N]
    undirected1 = dist1[0] + distN[i]
    undirected2 = dist1[i] + distN[0]
    d = min(directed, undirected1, undirected2)
    if d < INF:
        ans.append(d)
    else:
        ans.append(-1)

print(*ans)
