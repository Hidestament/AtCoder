"""
A - Exact Price
https://atcoder.jp/contests/abc223/tasks/abc223_a
"""

X = int(input())

print("Yes" if (X >= 100) and (X % 100 == 0) else "No")
