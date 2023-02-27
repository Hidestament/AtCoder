"""
E - Find Permutation
https://atcoder.jp/contests/abc291/tasks/abc291_e
"""
from collections import deque


N, M = map(int, input().split())
graph = [[] for _ in range(N)]
# 頂点vに入っている辺の本数
in_deg = {i: 0 for i in range(N)}
for _ in range(M):
    x, y = map(int, input().split())
    x -= 1
    y -= 1

    in_deg[y] += 1
    graph[x].append(y)


dq = deque([v for v in range(N) if in_deg[v] == 0])
dist = [-1] * N
dist[dq[0]] = 1

while dq:
    if len(dq) != 1:
        print("No")
        exit()

    now = dq.popleft()
    for to in graph[now]:
        in_deg[to] -= 1
        if in_deg[to] == 0:
            dq.append(to)
            dist[to] = dist[now] + 1

print("Yes")
print(*dist)
