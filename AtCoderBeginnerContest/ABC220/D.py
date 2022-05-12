"""
D - FG operation
https://atcoder.jp/contests/abc220/tasks/abc220_d
"""
N = int(input())
A = list(map(int, input().split()))
MOD = 998244353

# DP[i][x]: i回目の操作で左端の値がx(0 ~ 9)となる数
DP = [[0] * 10 for _ in range(N)]
DP[0][A[0]] = 1

for i in range(1, N):
    right = A[i]
    for left in range(10):
        # F操作
        DP[i][(left + right) % 10] += DP[i - 1][left]
        DP[i][(left + right) % 10] %= MOD
        # G操作
        DP[i][(left * right) % 10] += DP[i - 1][left]
        DP[i][(left * right) % 10] %= MOD

print(*DP[-1])
