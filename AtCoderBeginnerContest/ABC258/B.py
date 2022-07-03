"""
B - Number Box
https://atcoder.jp/contests/abc258/tasks/abc258_b
"""

from itertools import product


N = int(input())
A = [list(input()) for _ in range(N)]


move_i = [1, 1, 1, 0, 0, -1, -1, -1]
move_j = [1, 0, -1, 1, -1, 0, 1, -1]


def solve(i, j):
    ans = 0
    for di, dj in zip(move_i, move_j):
        score = ""
        for _ in range(N):
            score += A[i][j]
            i = (i + di) % N
            j = (j + dj) % N
        ans = max(ans, int(score))
    return ans


ans = 0
for i, j in product(range(N), range(N)):
    ans = max(ans, solve(i, j))

print(ans)
