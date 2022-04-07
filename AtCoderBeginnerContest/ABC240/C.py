"""
C - Jumping Takahashi
https://atcoder.jp/contests/abc240/tasks/abc240_c
部分和問題
"""

N, X = map(int, input().split())
jump = [list(map(int, input().split())) for _ in range(N)]

# DP[i][x]: i番目までを使って和をxにできるか
DP = [[0] * (X + 1) for _ in range(N+1)]
DP[0][0] = 1

for i in range(1, N+1):
    a, b = jump[i - 1]
    for x in range(X+1):
        # aを使う場合
        if x - a >= 0:
            DP[i][x] |= DP[i-1][x - a]

        # bを使う場合
        if x - b >= 0:
            DP[i][x] |= DP[i-1][x - b]


print("Yes" if DP[-1][X] else "No")
