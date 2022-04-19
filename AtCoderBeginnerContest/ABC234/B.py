"""
B - Longest Segment
https://atcoder.jp/contests/abc234/tasks/abc234_b
"""

N = int(input())
points = [list(map(int, input().split())) for _ in range(N)]


def dist(x1, y1, x2, y2):
    return (x1 - x2)**2 + (y1 - y2)**2


ans = 0
for x1, y1 in points:
    for x2, y2 in points:
        ans = max(ans, dist(x1, y1, x2, y2))

print(ans**0.5)
