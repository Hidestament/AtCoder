"""
A - Square Inequality
https://atcoder.jp/contests/abc199/tasks/abc199_a
"""

A, B, C = map(int, input().split())
print("Yes" if A**2 + B**2 < C**2 else "No")
