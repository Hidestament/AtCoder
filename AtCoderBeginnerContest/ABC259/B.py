"""
B - Counterclockwise Rotation
https://atcoder.jp/contests/abc259/tasks/abc259_b
"""

import math

a, b, d = map(int, input().split())

points = complex(a, b)

theta = math.radians(d)
ans = points * complex(math.cos(theta), math.sin(theta))

print(ans.real, ans.imag)
