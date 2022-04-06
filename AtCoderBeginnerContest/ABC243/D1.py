"""
D - Moves on Binary Tree
問題リンク: https://atcoder.jp/contests/abc243/tasks/abc243_d
2進数で解く
"""

from collections import deque


N, X = map(int, input().split())
S = str(input())

dq = deque(bin(X)[2:])
for s in S:
    if s == "L":
        dq.append("0")
    elif s == "R":
        dq.append("1")
    else:
        dq.pop()

print(int("".join(dq), 2))
