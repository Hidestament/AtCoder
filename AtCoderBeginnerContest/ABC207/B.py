"""
B - Hydrate
https://atcoder.jp/contests/abc207/tasks/abc207_b
"""

A, B, C, D = map(int, input().split())
if D * C - B <= 0:
    print(-1)
else:
    print(-(-A // (D * C - B)))
