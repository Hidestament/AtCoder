"""
E - Magical Ornament
https://atcoder.jp/contests/abc190/tasks/abc190_e
"""

from itertools import product
from collections import deque

INF = 10**15

N, M = map(int, input().split())
graph = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)

K = int(input())
C = list(map(lambda x: int(x) - 1, input().split()))
set_C = set(C)


def dfs(start):
    dq = deque([start])
    dist = [INF] * N
    dist[start] = 0
    seen = set([start])
    while dq:
        if len(seen) == K:
            break
        now = dq.popleft()
        for to in graph[now]:
            if dist[to] != INF:
                continue
            dist[to] = dist[now] + 1
            dq.append(to)
            if to in set_C:
                seen.add(to)
    return dist


dist = [[INF] * K for _ in range(K)]
for i in range(K):
    d = dfs(C[i])
    for j in range(K):
        dist[i][j] = d[C[j]]

DP = [[INF] * K for _ in range(1 << K)]

# 任意のC[i]からstartしたとする
for i in range(K):
    DP[1 << i][i] = 0

# DP[s][u] -> DP[s cup v][v]
for s in range(1 << K):
    # u -> v
    for u, v in product(range(K), range(K)):
        # s == 0ならどこでも行ける
        # s != 0のとこなら, uは訪問済じゃないとダメ
        if (s != 0) and not (s & (1 << u)):
            continue

        # vは訪問済でない
        if not (s & (1 << v)) and v != u:
            DP[s | (1 << v)][v] = min(DP[s | (1 << v)][v], DP[s][u] + dist[u][v])


ans = min(DP[-1][i] for i in range(K))
print(ans + 1 if ans < INF else -1)
