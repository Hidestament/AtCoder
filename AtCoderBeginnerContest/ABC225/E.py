"""
E - フ
https://atcoder.jp/contests/abc225/tasks/abc225_e
参考: https://zenn.dev/m193h/articles/20211030sat230551m193habc225#e---7
実際にはatanで角度を求めるが, tanは0 ~ 90°で狭義単調増加なので, tanの値でやっていってOK
Decimalじゃないと誤差でWAになる. PypyだとTLEになる
"""

from decimal import Decimal


N = int(input())
points = []
for _ in range(N):
    x, y = map(Decimal, input().split())
    if x - 1 == 0:
        theta2 = float("INF")
    else:
        theta2 = y / (x - 1)

    theta1 = (y - 1) / x
    points.append([theta1, theta2])

points.sort(key=lambda x: x[1])
last = -1
ans = 0
for theta1, theta2 in points:
    if last <= theta1:
        ans += 1
        last = theta2

print(ans)
