"""
C - Knight Fork
https://atcoder.jp/contests/abc239/tasks/abc239_c
"""

from itertools import product


def get_points(x, y):
    points = set()
    for dx, dy in product(range(-2, 3), range(-2, 3)):
        if dx**2 + dy**2 == 5:
            points.add((x+dx, y+dy))
    return points


x1, y1, x2, y2 = map(int, input().split())
points1 = get_points(x1, y1)
points2 = get_points(x2, y2)

print("Yes" if len(points1 & points2) else "No")
