"""
D - National Railway
https://atcoder.jp/contests/abc210/tasks/abc210_d
参考: https://note.com/momomo0214/n/na2ca58906c3f
"""
from itertools import product


def rotate(A):
    return [list(x)[::-1] for x in zip(*A)]


H, W, C = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]
INF = 10**15
ans = INF


def solve(A):
    ans = 10**15

    # DP[h][w]: (0 ~ h, 0 ~ w)のA[h][w] - C*(h + w)の最小値
    DP = [[INF] * len(A[0]) for _ in range(len(A))]
    for h, w in product(range(len(A)), range(len(A[0]))):
        if (h == 0) and (w == 0):
            continue
        elif h == 0:
            left = A[h][w - 1] - C * (h + w - 1)
            DP[h][w] = min(DP[h][w], DP[h][w - 1], left)
        elif w == 0:
            up = A[h - 1][w] - C * (h - 1 + w)
            DP[h][w] = min(DP[h][w], DP[h - 1][w], up)
        else:
            up = A[h - 1][w] - C * (h - 1 + w)
            left = A[h][w - 1] - C * (h + w - 1)
            DP[h][w] = min(DP[h][w], DP[h - 1][w], DP[h][w - 1], left, up)

    for h, w in product(range(len(A)), range(len(A[0]))):
        hw_value = A[h][w] + C * (h + w)
        min_hw_value = DP[h][w]
        ans = min(ans, hw_value + min_hw_value)
    return ans


for _ in range(2):
    A = rotate(A)
    ans = min(ans, solve(A))

print(ans)
