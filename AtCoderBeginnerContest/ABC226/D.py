"""
D - Teleportation
https://atcoder.jp/contests/abc226/tasks/abc226_d
"""

from itertools import permutations
from math import gcd


N = int(input())
points = [list(map(int, input().split())) for _ in range(N)]

ans = set()
for p1, p2 in permutations(points, 2):
    # i -> j ベクトル (a, b)
    a = p2[0] - p1[0]
    b = p2[1] - p1[1]

    c = gcd(abs(a), abs(b))
    ans.add((a//c, b//c))

print(len(ans))
