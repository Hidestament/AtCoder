"""
D - Game in Momotetsu World
https://atcoder.jp/contests/abc201/tasks/abc201_d
"""
from itertools import product

H, W = map(int, input().split())
A = [input() for _ in range(H)]
table = {"+": 1, "-": -1}
A = [[table[A[h][w]] for w in range(W)] for h in range(H)]

# DP[h][w]: (h, w)にいるときの最適行動した際のTakahashi - Aokiの値
DP = [[0] * W for _ in range(H)]
for h, w in product(range(H)[::-1], range(W)[::-1]):
    if (h + w) % 2 == 0:  # Takahashiの行動 -> 最大化
        if (h == H - 1) and (w == W - 1):
            DP[h][w] = 0
        elif h == H - 1:
            DP[h][w] = DP[h][w + 1] + A[h][w + 1]
        elif w == W - 1:
            DP[h][w] = DP[h + 1][w] + A[h + 1][w]
        else:
            DP[h][w] = max(DP[h + 1][w] + A[h + 1][w], DP[h][w + 1] + A[h][w + 1])

    else:  # Aokiの行動 -> 最小化
        if (h == H - 1) and (w == W - 1):
            DP[h][w] = 0
        elif h == H - 1:
            DP[h][w] = DP[h][w + 1] - A[h][w + 1]
        elif w == W - 1:
            DP[h][w] = DP[h + 1][w] - A[h + 1][w]
        else:
            DP[h][w] = min(DP[h + 1][w] - A[h + 1][w], DP[h][w + 1] - A[h][w + 1])

if DP[0][0] == 0:
    print("Draw")
elif DP[0][0] > 0:
    print("Takahashi")
else:
    print("Aoki")
