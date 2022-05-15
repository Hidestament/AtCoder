"""
F - Two Spanning Trees
https://atcoder.jp/contests/abc251/tasks/abc251_f
T1: 深さ優先探索木
T2: 幅優先探索木
"""
import sys
from collections import deque

sys.setrecursionlimit(10**7)


N, M = map(int, input().split())
graph = [[] for _ in range(N)]
for i in range(M):
    u, v = map(int, input().split())
    graph[u - 1].append(v - 1)
    graph[v - 1].append(u - 1)


def dfs(now):
    seen[now] = 1
    for to in graph[now]:
        if seen[to]:
            continue
        seen[to] = 1
        t1.append([now + 1, to + 1])
        dfs(to)


def bfs(now):
    dq = deque([now])
    seen = [0] * N
    seen[now] = 1
    tree = []
    while dq:
        now = dq.popleft()
        for to in graph[now]:
            if seen[to]:
                continue
            seen[to] = 1
            tree.append([now + 1, to + 1])
            dq.append(to)
    return tree


seen = [0] * N
t1 = []
dfs(0)
t2 = bfs(0)

for edge in t1:
    print(*edge)
for edge in t2:
    print(*edge)
