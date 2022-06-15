"""
E - Traveler
https://atcoder.jp/contests/abc197/tasks/abc197_e
"""
from collections import defaultdict

LEFT, RIGHT = 0, 1
INF = 10**10

N = int(input())
points = defaultdict(list)
for _ in range(N):
    x, c = map(int, input().split())
    points[c].append(x)

# Start地点 (x, c) = (0, 0)
points[0].append(0)
# End地点 (x, c) = (0, N + 1)
points[N + 1].append(0)

# 左端と右端の地点のみを考えれば良い
for c in points:
    sort_c = sorted(points[c])
    points[c] = [sort_c[0], sort_c[-1]]


# DP[c][LEFT or RIGHT]: color cの全てのボールを最終地点を(LEFT or RIGHT)で終了したときの最小時刻
DP = [[INF] * 2 for _ in range(N + 2)]
DP[0] = [0, 0]

sort_color = sorted(points.keys())
for i, c in enumerate(sort_color[1:], start=1):
    left_points, right_points = points[c]
    dist = right_points - left_points
    before_c = sort_color[i - 1]

    # LEFT -> LEFT
    DP[c][LEFT] = DP[before_c][LEFT] + abs(points[before_c][LEFT] - right_points) + dist

    # LEFT -> RIGHT
    DP[c][RIGHT] = DP[before_c][LEFT] + abs(points[before_c][LEFT] - left_points) + dist

    # RIGHT -> LEFT
    DP[c][LEFT] = min(
        DP[c][LEFT],
        DP[before_c][RIGHT] + abs(points[before_c][RIGHT] - right_points) + dist,
    )

    # RIGHT -> RIGHT
    DP[c][RIGHT] = min(
        DP[c][RIGHT],
        DP[before_c][RIGHT] + abs(points[before_c][RIGHT] - left_points) + dist,
    )

print(DP[N + 1][0])
