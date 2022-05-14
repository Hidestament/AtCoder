"""
C - Many Balls
https://atcoder.jp/contests/abc216/tasks/abc216_c
"""
from collections import deque

N = int(input())
dq = deque()

while N != 0:
    if N % 2 == 0:
        N //= 2
        dq.appendleft("B")
    else:
        N -= 1
        dq.appendleft("A")

print("".join(dq))
