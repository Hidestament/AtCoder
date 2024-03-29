"""
C - Dice Sum
https://atcoder.jp/contests/abc248/tasks/abc248_c
貰うDP O(N*M*K)
"""

N, M, K = map(int, input().split())
mod = 998244353

# DP[i][k]: i項目まで考えたときに和がkとなるようなモノ
DP = [[0 for _ in range(K+1)] for _ in range(N+1)]
DP[0][0] = 1

for i in range(1, N+1):  # 現在考えている項
    for k in range(1, K + 1):  # 現在の項までの和
        for num in range(1, M+1):  # 現在の項に何の数字を入れるか
            if k - num >= 0:
                DP[i][k] += DP[i-1][k - num]
                DP[i][k] %= mod
print(sum(DP[-1]) % mod)
