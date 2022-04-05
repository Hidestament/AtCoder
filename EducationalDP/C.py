"""
C - Vacation
問題リンク: https://atcoder.jp/contests/dp/tasks/dp_c
"""

from itertools import product


N = int(input())
activity = [list(map(int, input().split())) for _ in range(N)]

# DP[i][active]: 日にちiにacutiveを選んだときの最適値
DP = [[0] * 3 for _ in range(N)]
for active in range(3):
    DP[0][active] = activity[0][active]

for i in range(1, N):
    for bef, aft in product(range(3), range(3)):
        if bef == aft:
            continue
        DP[i][aft] = max(DP[i][aft], DP[i-1][bef] + activity[i][aft])

print(max(DP[-1]))
