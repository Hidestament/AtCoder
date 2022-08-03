"""
D - Flipping and Bonus
https://atcoder.jp/contests/abc261/tasks/abc261_d
"""

from collections import defaultdict


N, M = map(int, input().split())
X = list(map(int, input().split()))
bonus = defaultdict(int)
for _ in range(M):
    c, y = map(int, input().split())
    bonus[c] = y


# DP[i][cnt]: i回目にカウンターがcntの際の最大値
DP = [[0] * (N + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    # i回目のコイントスが裏の場合
    DP[i][0] = max(DP[i][0], max(DP[i - 1]))

    # i回目のコイントスが表の場合
    for cnt in range(1, i + 1):
        DP[i][cnt] = max(DP[i][cnt], DP[i - 1][cnt - 1] + X[i - 1] + bonus[cnt])

print(max(DP[-1]))
