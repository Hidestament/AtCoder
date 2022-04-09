"""
F - |LIS| = 3
https://atcoder.jp/contests/abc237/tasks/abc237_f
LISの復元的なことをやる
"""

from itertools import product


N, M = map(int, input().split())
mod = 998244353

# DP[i][x][y][z]: i項からなる配列の中で, LIS配列が(x, y, z) となるようなモノの個数
DP = [[[[0] * (M+1) for _ in range(M+1)] for _ in range(M+1)]
      for _ in range(N+1)]

# x = M の場合は∞がLIS配列に入っているとする
DP[0][M][M][M] = 1

# 配るDP
for i in range(N):
    # nはi項目に入る数字
    for n in range(M):
        for x, y, z in product(range(M+1), range(M+1), range(M+1)):
            if not (x <= y <= z):
                continue
            p = DP[i][x][y][z]
            if n <= x:
                DP[i+1][n][y][z] += p
                DP[i+1][n][y][z] %= mod
            elif n <= y:
                DP[i+1][x][n][z] += p
                DP[i+1][x][n][z] %= mod
            elif n <= z:
                DP[i+1][x][y][n] += p
                DP[i+1][x][y][n] %= mod

ans = 0
for x, y, z in product(range(M), range(M), range(M)):
    if x <= y <= z:
        ans += DP[N][x][y][z]
        ans %= mod

print(ans)
