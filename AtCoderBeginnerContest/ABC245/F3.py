"""
F - Endless Walk
問題リンク: https://atcoder.jp/contests/abc245/tasks/abc245_f
出次数0の頂点を消していく
"""

from collections import deque


N, M = map(int, input().split())
graph = [[] for _ in range(N)]
outdeg = [0] * N

# 辺を逆向きに貼ると削除しやすい
for _ in range(M):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    graph[v].append(u)
    outdeg[u] += 1

dq = deque([v for v in range(N) if outdeg[v] == 0])
ans = N
while dq:
    ans -= 1
    now = dq.popleft()
    for to in graph[now]:
        outdeg[to] -= 1
        if outdeg[to] == 0:
            dq.append(to)

print(ans)
