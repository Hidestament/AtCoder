"""
A - Difference Max
https://atcoder.jp/contests/abc196/tasks/abc196_a
"""

a, b = map(int, input().split())
c, d = map(int, input().split())

print(max(b - d, b - c, a - c, a - d))
