"""
B - Mongeness
https://atcoder.jp/contests/abc224/tasks/abc224_b
"""

from itertools import product


H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]


def check():
    for i1, j1 in product(range(H-1), range(W-1)):
        for i2, j2 in product(range(i1+1, H), range(j1+1, W)):
            if A[i1][j1] + A[i2][j2] > A[i2][j1] + A[i1][j2]:
                return False
    return True


print("Yes" if check() else "No")
