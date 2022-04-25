"""
D - Longest X
https://atcoder.jp/contests/abc229/tasks/abc229_d
尺取法で解ける
"""

from collections import deque


S = str(input())
K = int(input())

dq = deque()
ans = 0
num_dot = 0
for s in S:
    if s == ".":
        num_dot += 1
    dq.append(s)
    while dq and (num_dot > K):
        rm = dq.popleft()
        if rm == ".":
            num_dot -= 1
    ans = max(ans, len(dq))

print(ans)
