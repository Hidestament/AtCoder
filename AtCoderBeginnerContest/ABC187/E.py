"""
E - Through Path
https://atcoder.jp/contests/abc187/tasks/abc187_e
"""

from collections import deque


N = int(input())
edges = []
graph = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    edges.append([a - 1, b - 1])
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)

depth = [-1] * N
depth[0] = 0
dq = deque([0])
while dq:
    now = dq.popleft()
    for to in graph[now]:
        if depth[to] != -1:
            continue
        depth[to] = depth[now] + 1
        dq.append(to)


X = [0] * N
Q = int(input())
for _ in range(Q):
    t, e, x = map(int, input().split())
    ae, be = edges[e - 1]

    if t == 2:
        ae, be = be, ae

    if depth[ae] > depth[be]:
        X[ae] += x
    else:
        X[0] += x
        X[be] -= x


C = [-1] * N
C[0] = X[0]
dq = deque([[0, X[0]]])
while dq:
    now, x = dq.popleft()
    for to in graph[now]:
        if C[to] != -1:
            continue
        next_x = x + X[to]
        C[to] = next_x
        dq.append([to, next_x])

print(*C)
