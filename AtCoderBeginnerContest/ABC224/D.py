"""
D - 8 Puzzle on Graph
https://atcoder.jp/contests/abc224/tasks/abc224_d
"""

from collections import deque, defaultdict


M = int(input())
graph = [[] for _ in range(10)]
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

P = list(map(int, input().split()))
now = [-1] * 9
for i, p in enumerate(P, start=1):
    now[p - 1] = i

ans = [1, 2, 3, 4, 5, 6, 7, 8, -1]
dist = defaultdict(int)
dist[tuple(now)] = 0

dq = deque([now])
while dq:
    now = dq.popleft()
    if now == ans:
        break
    blank = now.index(-1) + 1

    for to in graph[blank]:
        next_pos = now[::]
        next_pos[blank-1], next_pos[to-1] = next_pos[to-1], next_pos[blank-1]
        if tuple(next_pos) not in dist:
            dist[tuple(next_pos)] = dist[tuple(now)] + 1
            dq.append(next_pos)

print(dist[tuple(ans)] if tuple(ans) in dist else -1)
