"""
B - Enlarged Checker Board
https://atcoder.jp/contests/abc250/tasks/abc250_b
"""
from itertools import product


N, A, B = map(int, input().split())
grid = [[0] * (B * N) for _ in range(A * N)]

# 縦i, 横j: 現在のマス = (i*A, j*B)
for i, j in product(range(N), range(N)):
    if (i + j) % 2 == 0:
        color = "."
    else:
        color = "#"
    for a, b in product(range(A), range(B)):
        grid[i * A + a][j * B + b] = color

for i in range(A * N):
    print("".join(grid[i]))
