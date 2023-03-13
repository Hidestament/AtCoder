"""
C - Ladder Takahashi
https://atcoder.jp/contests/abc277/tasks/abc277_c
"""
from collections import deque, defaultdict


N = int(input())
graph = defaultdict(list)
for _ in range(N):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


dist = {}
dq = deque([1])
while dq:
    now = dq.popleft()

    if now in dist:
        continue
    dist[now] = 1

    for to in graph[now]:
        if to in dist:
            continue
        dq.append(to)


print(max(dist.keys()))
