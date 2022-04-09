"""
D - LR insertion
https://atcoder.jp/contests/abc237/tasks/abc237_d
"""

from collections import deque


N = int(input())
S = str(input())

dq = deque([N])
for i in range(N)[::-1]:
    if S[i] == "L":
        dq.append(i)
    else:
        dq.appendleft(i)

print(*dq)
