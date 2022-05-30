"""
E - Safety Journey
https://atcoder.jp/contests/abc212/tasks/abc212_e
"""
N, M, K = map(int, input().split())
MOD = 998244353
edges = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v = map(int, input().split())
    edges[u].append(v)
    edges[v].append(u)

# DP[k][i]: k日目に都市iにいる場合の数
DP = [[0] * (N + 1) for _ in range(K + 1)]
DP[0][1] = 1  # 0日目は1Start


def calc_acc(dp):
    acc = [0] * (N + 1)
    for prev in range(1, N + 1):
        for to in edges[prev]:
            acc[to] += dp[prev]
    return acc


acc = calc_acc(DP[0])
for k in range(1, K + 1):
    s = sum(DP[k - 1])
    # 全体 - 旅(i -> i) - ∑j EDGE(j -> i)
    for i in range(1, N + 1):
        DP[k][i] += s - DP[k - 1][i] - acc[i]
        DP[k][i] %= MOD
    acc = calc_acc(DP[k])


print(DP[K][1])
