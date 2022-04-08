"""
A - Exponential or Quadratic
https://atcoder.jp/contests/abc238/tasks/abc238_a
"""

n = int(input())
print("Yes" if pow(2, n) > pow(n, 2) else "No")
