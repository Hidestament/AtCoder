"""
C - Dice Sum
https://atcoder.jp/contests/abc248/tasks/abc248_c
貰うDP + 累積和 O(N * K)
"""

from itertools import accumulate


N, M, K = map(int, input().split())
mod = 998244353

# DP[i][k]: i項目まで考えたときに和がkとなるようなモノ
DP = [[0 for _ in range(K+1)] for _ in range(N+1)]
DP[0][0] = 1
acc = [0] + list(accumulate(DP[0]))

for i in range(1, N+1):  # 現在考えている項
    for k in range(1, K + 1):  # 現在の項までの和
        DP[i][k] = (acc[k] - acc[max(0, k - M)])
        DP[i][k] %= mod

    # accの更新
    acc = [0] + list(accumulate(DP[i]))

print(sum(DP[-1]) % mod)
