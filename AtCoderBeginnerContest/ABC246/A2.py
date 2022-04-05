"""
A - Four Points
問題リンク: https://atcoder.jp/contests/abc246/tasks/abc246_a
頑張って解く
"""

points = sorted([list(map(int, input().split())) for _ in range(3)])

if points[0][0] == points[1][0]:
    x4 = points[2][0]
else:
    x4 = points[0][0]

points.sort(key=lambda x: x[1])
if points[0][1] == points[1][1]:
    y4 = points[2][1]
else:
    y4 = points[0][1]

print(x4, y4)
