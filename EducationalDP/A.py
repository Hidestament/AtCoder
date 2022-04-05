"""
A - Frog 1
問題リンク: https://atcoder.jp/contests/dp/tasks/dp_a
"""

N = int(input())
H = list(map(int, input().split()))

# DP[i]: i段目に到達する最適値
INF = 10**10
DP = [INF] * N
DP[0] = 0

for i in range(1, N):
    DP[i] = min(DP[i], DP[i-1] + abs(H[i] - H[i-1]))
    if i >= 2:
        DP[i] = min(DP[i], DP[i-2] + abs(H[i] - H[i-2]))

print(DP[-1])
