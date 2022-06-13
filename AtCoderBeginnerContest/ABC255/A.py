"""
A - You should output ARC, though this is ABC.
https://atcoder.jp/contests/abc255/tasks/abc255_a
"""

R, C = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(2)]

print(A[R - 1][C - 1])
