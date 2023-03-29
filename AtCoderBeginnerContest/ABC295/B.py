"""
B - Bombs
https://atcoder.jp/contests/abc295/tasks/abc295_b
"""
import sys
from itertools import product

input = sys.stdin.readline

R, C = map(int, input().split())
B = [str(input()) for _ in range(R)]

A = [[""] * C for _ in range(R)]

for r, c in product(range(R), range(C)):
    if B[r][c] == ".":
        A[r][c] = "."
    elif B[r][c] == "#":
        if A[r][c] == ".":
            continue
        A[r][c] = "#"
    else:
        dist = int(B[r][c])
        for rd, cd in product(range(R), range(C)):
            if abs(r - rd) + abs(c - cd) <= dist:
                A[rd][cd] = "."

for a in A:
    print("".join(a))
