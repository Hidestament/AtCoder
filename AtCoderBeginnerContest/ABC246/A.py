x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())


points = [[x1, y1], [x2, y2], [x3, y3]]
points.sort()

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
