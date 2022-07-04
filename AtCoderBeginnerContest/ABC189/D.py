"""
D - Logical Expression
https://atcoder.jp/contests/abc189/tasks/abc189_d
"""

N = int(input())
S = [input() for _ in range(N)]

# DP[i][bool]: y[i] = bool となるモノの個数
DP = [[0] * 2 for _ in range(N + 1)]
DP[0][0], DP[0][1] = 1, 1

for i in range(1, N + 1):
    if S[i - 1] == "AND":
        # xi = 0 としたとき
        DP[i][0] += DP[i - 1][0] + DP[i - 1][1]
        # xi = 1 としたとき
        DP[i][1] += DP[i - 1][1]
        DP[i][0] += DP[i - 1][0]
    else:
        # xi = 0 としたとき
        DP[i][0] += DP[i - 1][0]
        DP[i][1] += DP[i - 1][1]
        # xi = 1 としたとき
        DP[i][1] += DP[i - 1][0] + DP[i - 1][1]

print(DP[-1][1])
