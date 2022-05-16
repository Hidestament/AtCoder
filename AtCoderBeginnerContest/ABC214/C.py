"""
C - Distribution
https://atcoder.jp/contests/abc214/tasks/abc214_c
"""

N = int(input())
S = list(map(int, input().split()))
T = list(map(int, input().split()))


INF = 10**15
# DP[i]: i番目のスヌケの最小値
DP = [INF] * N

start_i = T.index(min(T))
DP[start_i] = min(T)

i = start_i
for _ in range(N):
    DP[(i + 1) % N] = min(DP[i] + S[i], T[(i + 1) % N])
    i = (i + 1) % N

print(*DP, sep="\n")
