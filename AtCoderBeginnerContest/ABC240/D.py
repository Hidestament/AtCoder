"""
D - Strange Balls
https://atcoder.jp/contests/abc240/tasks/abc240_d
"""

from collections import deque


N = int(input())
A = list(map(int, input().split()))

dq = deque()
top, top_num = deque([-1]), deque([-1])
for a in A:
    if a == top[-1]:
        top_num[-1] += 1
    else:
        top.append(a)
        top_num.append(1)

    dq.append(a)
    if top[-1] == top_num[-1]:
        for _ in range(top[-1]):
            dq.pop()
        top_num[-1] -= top[-1]
        if top_num[-1] == 0:
            top_num.pop()
            top.pop()

    print(len(dq))
