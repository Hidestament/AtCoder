"""
B - Matrix Transposition
https://atcoder.jp/contests/abc237/tasks/abc237_b
"""

H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]


def transpose(A):
    return [list(x) for x in zip(*A)]


for x in transpose(A):
    print(*x)
