"""
D - Collision
https://atcoder.jp/contests/abc209/tasks/abc209_d
"""
from collections import deque


N, Q = map(int, input().split())
graph = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)

# 根からの最短路を求める
dist = [-1] * N
dist[0] = 0
dq = deque([0])
while dq:
    now = dq.popleft()
    for to in graph[now]:
        if dist[to] != -1:
            continue
        dist[to] = dist[now] + 1
        dq.append(to)

for _ in range(Q):
    c, d = map(int, input().split())
    print("Town" if abs(dist[c - 1] - dist[d - 1]) % 2 == 0 else "Road")
