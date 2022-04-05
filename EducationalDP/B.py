"""
B - Frog 2
問題リンク: https://atcoder.jp/contests/dp/tasks/dp_b
"""

N, K = map(int, input().split())
H = list(map(int, input().split()))

# DP[i]: i段目にたどり着く最適値
INF = 10**10
DP = [INF] * N
DP[0] = 0

for i in range(N - 1):
    for k in range(1, K+1):
        if i + k < N:
            DP[i + k] = min(DP[i + k], DP[i] + abs(H[i] - H[i + k]))

print(DP[-1])
