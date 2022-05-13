"""
F - Blocked Roads
https://atcoder.jp/contests/abc218/tasks/abc218_f
"""
from collections import deque

N, M = map(int, input().split())
graph = [[] for _ in range(N)]
for i in range(M):
    s, t = map(int, input().split())
    graph[s - 1].append([t - 1, i])


# 通常の最短路を求める
def bfs(ng_edge=-1):
    dist = [-1] * N
    prev = [-1] * N
    dq = deque([0])
    dist[0] = 0
    while dq:
        now = dq.popleft()
        for to, i in graph[now]:
            if dist[to] != -1:
                continue
            if i == ng_edge:
                continue
            dist[to] = dist[now] + 1
            prev[to] = [now, i]
            dq.append(to)
    return dist, prev


def restore():
    # 経路復元
    path = set()
    now = N - 1
    if restore:
        while now != 0:
            to, i = prev[now]
            path.add(i)
            now = to
    return path


dist, prev = bfs()
if dist[N - 1] == -1:
    for _ in range(M):
        print(-1)
    exit()


path = restore()
for i in range(M):
    if i not in path:
        print(dist[N - 1])
    else:
        d, _ = bfs(i)
        print(d[N - 1])
