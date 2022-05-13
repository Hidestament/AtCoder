"""
C - Shapes
https://atcoder.jp/contests/abc218/tasks/abc218_c
"""
from itertools import product


N = int(input())
S = [list(input()) for _ in range(N)]
T = [list(input()) for _ in range(N)]


def get_left_up(A):
    for h, w in product(range(N), range(N)):
        if A[h][w] == "#":
            return (h, w)


def get_grid_set(A):
    offset_h, offset_w = get_left_up(A)
    s = set()
    for h, w in product(range(N), range(N)):
        if A[h][w] == "#":
            s.add((h - offset_h, w - offset_w))
    return s


def check(A, B):
    a_set = get_grid_set(A)
    b_set = get_grid_set(B)
    return a_set == b_set


def rotate(A):
    return [list(x)[::-1] for x in zip(*A)]


flag = False
for _ in range(4):
    T = rotate(T)
    flag |= check(S, T)

print("Yes" if flag else "No")
