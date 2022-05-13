"""
D - Strange Lunchbox
https://atcoder.jp/contests/abc219/tasks/abc219_d
"""
from itertools import product


N = int(input())
INF = 10**15
X, Y = map(int, input().split())
lunch = [list(map(int, input().split())) for _ in range(N)]

# DP[i][x][y]: i番目まで見たときに, たこ焼きx個 たいやきy個となる最小値
DP = [[[INF] * (Y + 1) for _ in range(X + 1)] for _ in range(N + 1)]
DP[0][0][0] = 0

# 配るDP
for i in range(N):
    a, b = lunch[i]
    for x, y in product(range(X + 1), range(Y + 1)):
        # その弁当を使用するとき
        DP[i + 1][min(X, x + a)][min(Y, y + b)] = min(
            DP[i + 1][min(X, x + a)][min(Y, y + b)], DP[i][x][y] + 1
        )

        # 使用しないとき
        DP[i + 1][x][y] = min(DP[i + 1][x][y], DP[i][x][y])

ans = DP[N][X][Y]
print(ans if ans != INF else -1)
