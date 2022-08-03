"""
B - Tournament Result
https://atcoder.jp/contests/abc261/tasks/abc261_b
"""

from itertools import product


N = int(input())
A = [list(input()) for _ in range(N)]

for i, j in product(range(N), range(N)):
    if A[i][j] == "W":
        A[i][j] = 1
    elif A[i][j] == "L":
        A[i][j] = -1
    else:
        A[i][j] = 0


correct = True
for i, j in product(range(N), range(N)):
    if A[i][j] + A[j][i] != 0:
        correct = False

print("correct" if correct else "incorrect")
