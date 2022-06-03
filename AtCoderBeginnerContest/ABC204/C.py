"""
C - Tour
https://atcoder.jp/contests/abc204/tasks/abc204_c
"""
from collections import deque

N, M = map(int, input().split())
graph = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a - 1].append(b - 1)


def bfs(start):
    dq = deque([start])
    dist = [-1] * N
    dist[start] = 0
    while dq:
        now = dq.popleft()
        for to in graph[now]:
            if dist[to] != -1:
                continue
            dist[to] = dist[now] + 1
            dq.append(to)
    return dist


ans = 0
for v in range(N):
    dist = bfs(v)
    ans += sum(d >= 0 for d in dist)

print(ans)
