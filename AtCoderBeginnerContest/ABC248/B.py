"""
B - Slimes
https://atcoder.jp/contests/abc248/tasks/abc248_b
"""

A, B, K = map(int, input().split())

cnt = 0
while A < B:
    A *= K
    cnt += 1
print(cnt)
