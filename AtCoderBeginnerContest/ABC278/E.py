"""
E - Grid Filling
https://atcoder.jp/contests/abc278/tasks/abc278_e
"""
from itertools import product
import sys

input = sys.stdin.readline


H, W, N, h, w = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]


def generate(A):
    s = [[[0] * (N + 1) for _ in range(W)] for _ in range(H)]
    for h, w in product(range(H), range(W)):
        a = A[h][w]
        if (h == 0) and (w == 0):
            s[h][w][a] += 1
        elif h == 0:
            s[h][w] = [s[h][w - 1][x] for x in range(N + 1)]
            s[h][w][a] += 1
        elif w == 0:
            s[h][w] = [s[h - 1][w][x] for x in range(N + 1)]
            s[h][w][a] += 1
        else:
            s[h][w] = [
                s[h][w - 1][x] + s[h - 1][w][x] - s[h - 1][w - 1][x]
                for x in range(N + 1)
            ]
            s[h][w][a] += 1
    return s


def calc_2d_sum(h1, w1, h2, w2):
    """(h1, w1) ~ (h2, w2)の総和 (境界を含む)"""
    if (h1 > h2) or (w1 > w2):
        return 0
    if (h1 == 0) and (w1 == 0):
        return s[h2][w2]
    if h1 == 0:
        count = [s[h2][w2][a] - s[h2][w1 - 1][a] for a in range(N + 1)]
        return count
    if w1 == 0:
        count = [s[h2][w2][a] - s[h1 - 1][w2][a] for a in range(N + 1)]
        return count

    count = [
        s[h2][w2][a] - s[h2][w1 - 1][a] - s[h1 - 1][w2][a] + s[h1 - 1][w1 - 1][a]
        for a in range(N + 1)
    ]
    return count


s = generate(A)
all_grid = s[H - 1][W - 1]

ans = [[-1] * (W - w + 1) for _ in range(H - h + 1)]
for k, l in product(range(H - h + 1), range(W - w + 1)):
    h1, w1 = k, l
    h2, w2 = k + h - 1, l + w - 1

    black_grid = calc_2d_sum(h1, w1, h2, w2)

    count = [all_grid[i] - black_grid[i] for i in range(1, N + 1)]
    ans[k][l] = sum(a > 0 for a in count)


for i in ans:
    print(*i)
