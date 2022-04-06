"""
C - 1111gal password
問題リンク: https://atcoder.jp/contests/abc242/tasks/abc242_c
"""

N = int(input())
mod = 998244353

# DP[i][x]: i桁目をxとしたときの個数
DP = [[0] * 9 for _ in range(N)]
for x in range(9):
    DP[0][x] = 1

for i in range(1, N):
    for x in range(9):
        DP[i][x] += DP[i-1][x]
        if x != 0:
            DP[i][x] += DP[i-1][x-1]

        if x != 8:
            DP[i][x] += DP[i-1][x+1]

        DP[i][x] %= mod

print(sum(DP[-1]) % mod)
