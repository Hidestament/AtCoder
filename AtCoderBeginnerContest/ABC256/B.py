"""
B - Batters
https://atcoder.jp/contests/abc256/tasks/abc256_b
"""
from collections import deque

N = int(input())
A = list(map(int, input().split()))

P = 0
now_pos = deque()
for a in A:
    now_pos.append(0)
    next_pos = deque()
    while now_pos:
        now = now_pos.popleft()
        if a + now < 4:
            next_pos.append(a + now)
        else:
            P += 1

    now_pos = next_pos

print(P)
