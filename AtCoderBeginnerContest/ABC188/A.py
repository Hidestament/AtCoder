"""
A - Three-Point Shot
https://atcoder.jp/contests/abc188/tasks/abc188_a
"""

X, Y = map(int, input().split())

if min(X, Y) + 3 > max(X, Y):
    print("Yes")
else:
    print("No")
