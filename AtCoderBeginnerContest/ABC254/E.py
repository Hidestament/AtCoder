"""
E - Small d and k
https://atcoder.jp/contests/abc254/tasks/abc254_e
"""
from collections import deque, defaultdict


N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def bfs(start, k):
    dist = defaultdict(int)
    dist[start] = 0
    dq = deque([start])
    ans = 0
    while dq:
        now = dq.popleft()
        if dist[now] <= k:
            ans += now
        else:
            break

        for to in graph[now]:
            if to in dist:
                continue
            dist[to] = dist[now] + 1
            dq.append(to)
    return ans


Q = int(input())
for _ in range(Q):
    x, k = map(int, input().split())
    print(bfs(x, k))
