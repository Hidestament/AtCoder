"""
E - Peddler
https://atcoder.jp/contests/abc188/tasks/abc188_e
"""

INF = float("inf")


N, M = map(int, input().split())
A = list(map(int, input().split()))

graph = [[] for _ in range(N)]
for _ in range(M):
    x, y = map(int, input().split())
    graph[x - 1].append(y - 1)

# DP[i]: 都市i以降で売れる金の金額の最大値
DP = [-INF] * N

ans = -INF
for now in range(N)[::-1]:
    for to in graph[now]:
        DP[now] = max(DP[now], DP[to], A[to])
    ans = max(ans, DP[now] - A[now])

print(ans)
