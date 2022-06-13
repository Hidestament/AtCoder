"""
B - Light It Up
https://atcoder.jp/contests/abc255/tasks/abc255_b
"""

N, K = map(int, input().split())
A = list(map(int, input().split()))
points = [list(map(int, input().split())) for _ in range(N)]

ans = 0
for x, y in points:
    dist_min = 10**19
    for center in A:
        cx, cy = points[center - 1]
        dist = (cx - x) ** 2 + (cy - y) ** 2
        dist_min = min(dist_min, dist**0.5)
    ans = max(ans, dist_min)

print(ans)
