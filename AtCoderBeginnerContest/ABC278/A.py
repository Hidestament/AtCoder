"""
A - Shift
https://atcoder.jp/contests/abc278/tasks/abc278_a
"""
from collections import deque


N, K = map(int, input().split())
A = deque(list(map(int, input().split())))

for _ in range(K):
    A.popleft()
    A.append(0)

print(*A)
