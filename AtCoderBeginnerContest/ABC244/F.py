"""
F - Shortest Good Path
問題リンク: https://atcoder.jp/contests/abc244/tasks/abc244_f
"""

from collections import deque


N, M = map(int, input().split())
graph = [[] for _ in range(N)]
for _ in range(M):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    graph[u].append(v)
    graph[v].append(u)

INF = 10**10
# DP[bit][v]: 状態がbitで, 最後に訪れる頂点がvであるようなものの最短路
DP = [[INF] * N for _ in range(1 << N)]

dq = deque()
for i in range(N):
    DP[0][i] = 0
    bit = 1 << i
    DP[bit][i] = 1
    dq.append([bit, i])

while dq:
    bit, now = dq.popleft()
    for to in graph[now]:
        next_bit = bit ^ (1 << to)
        if DP[next_bit][to] > DP[bit][now] + 1:
            DP[next_bit][to] = DP[bit][now] + 1
            dq.append([next_bit, to])

ans = sum(min(DP[bit][v] for v in range(N)) for bit in range(1 << N))
print(ans)
