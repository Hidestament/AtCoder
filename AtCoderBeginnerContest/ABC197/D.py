"""
D - Opposite
https://atcoder.jp/contests/abc197/tasks/abc197_d
"""
import math

N = int(input())
x0, y0 = map(int, input().split())
xh, yh = map(int, input().split())

# 中心座標を(0, 0)に持っていく
xc, yc = (x0 + xh) / 2, (y0 + yh) / 2
x0 -= xc
y0 -= yc

# 左に N / 360度回転する
theta = math.radians(360 / N)
p0 = complex(x0, y0)
rotate = complex(math.cos(theta), math.sin(theta))
r = abs(rotate)

pn = (p0 * rotate) / r
print(pn.real + xc, pn.imag + yc)
