"""
D - Moves on Binary Tree
問題リンク: https://atcoder.jp/contests/abc243/tasks/abc243_d
不要な移動を削除する
"""

from collections import deque


N, X = map(int, input().split())
S = str(input())

dq = deque()
for s in S:
    if s == "U":
        if (dq) and (dq[-1] != "U"):
            dq.pop()
            continue
    dq.append(s)

while dq:
    s = dq.popleft()
    if s == "U":
        X //= 2
    elif s == "R":
        X = 2*X + 1
    else:
        X *= 2

print(X)
