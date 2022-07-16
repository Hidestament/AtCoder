"""
A - Growth Record
https://atcoder.jp/contests/abc259/tasks/abc259_a
"""

N, M, X, T, D = map(int, input().split())

base = T - X * D
print(base + D * min(X, M))
