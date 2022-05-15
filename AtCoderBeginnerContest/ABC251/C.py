"""
C - Poem Online Judge
https://atcoder.jp/contests/abc251/tasks/abc251_c
"""
N = int(input())
points = []
original = set()
for i in range(1, N + 1):
    s, t = map(str, input().split())
    if s in original:
        continue
    points.append([int(t), i])
    original.add(s)

points.sort(key=lambda x: (-x[0], x[1]))
print(points[0][1])
