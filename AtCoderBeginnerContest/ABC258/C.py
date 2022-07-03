"""
C - Rotation
https://atcoder.jp/contests/abc258/tasks/abc258_c
"""

N, Q = map(int, input().split())
S = str(input())

top = 0
for _ in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 1:
        top = (top - q[1]) % N
    else:
        print(S[(top + q[1] - 1) % N])
