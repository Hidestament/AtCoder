"""
D - Between Two Arrays
https://atcoder.jp/contests/abc222/tasks/abc222_d
"""
from itertools import accumulate


N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
MOD = 998244353

# DP[i][x]: i番目をxにしたときの個数
DP = [[0] * (3001) for _ in range(N + 1)]
DP[0][0] = 1
acc = list(accumulate(DP[0]))

for i in range(1, N + 1):
    a, b = A[i - 1], B[i - 1]
    for x in range(a, b + 1):
        DP[i][x] += acc[x]
        DP[i][x] %= MOD
    acc = list(accumulate(DP[i]))

print(sum(DP[N]) % MOD)
