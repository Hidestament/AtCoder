"""
D - Cooking
https://atcoder.jp/contests/abc204/tasks/abc204_d
"""

N = int(input())
T = list(map(int, input().split()))

S = sum(T) // 2

# DP[i][s]: i番目までの品物を選んだ際に, 和をsにできるか
DP = [[0] * (S + 1) for _ in range(N + 1)]
DP[0][0] = 1

for i in range(1, N + 1):
    t = T[i - 1]
    for s in range(S + 1):
        # 品物iを使用するとき
        if s - t >= 0:
            DP[i][s] |= DP[i - 1][s - t]
        # 使わないとき
        DP[i][s] |= DP[i - 1][s]


ans = 10**19
sum_s = sum(T)
for s in range(S + 1):
    if DP[-1][s]:
        cook_time = max(s, sum_s - s)
        ans = min(ans, cook_time)
print(ans)
