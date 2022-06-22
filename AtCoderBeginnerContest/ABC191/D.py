"""
D - Circle Lattice Points
https://atcoder.jp/contests/abc191/tasks/abc191_d
PypyだとTLE
"""
from decimal import Decimal


X, Y, R = map(Decimal, input().split())

x_lower = Decimal.__ceil__(X - R)
x_upper = Decimal.__floor__(X + R)

ans = 0
for x in range(x_lower, x_upper + 1):
    dist = Decimal.sqrt(R**2 - (X - x) ** 2)
    y_upper = Decimal.__floor__(Y + dist)
    y_lower = Decimal.__ceil__(Y - dist)
    ans += max(0, y_upper - y_lower + 1)

print(ans)
