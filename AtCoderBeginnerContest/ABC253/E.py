"""
E - Distance Sequence
https://atcoder.jp/contests/abc253/tasks/abc253_e
"""
from itertools import accumulate

N, M, K = map(int, input().split())
MOD = 998244353

# DP[i][x]: i項目をxとしたときの場合の数
DP = [[0] * (M + 1) for _ in range(N + 1)]
for x in range(1, M + 1):
    DP[1][x] = 1  # A1は 1 ~ M の範囲でOK
acc = list(accumulate(DP[1]))

for i in range(2, N + 1):
    s = acc[-1]
    for x in range(1, M + 1):
        if K == 0:
            DP[i][x] += s
            DP[i][x] %= MOD
        else:
            upper = x + (K - 1)
            lower = x - K
            DP[i][x] += s - (acc[min(M, upper)] - acc[max(0, lower)])
            DP[i][x] %= MOD
    acc = list(accumulate(DP[i]))

print(sum(DP[-1]) % MOD)
