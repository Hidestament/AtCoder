"""
C - Compass Walking
https://atcoder.jp/contests/abc198/tasks/abc198_c
"""

R, X, Y = map(int, input().split())

dist = (X**2 + Y**2) ** 0.5

if dist < R:
    print(2)
else:
    print(-int(-dist // R))
