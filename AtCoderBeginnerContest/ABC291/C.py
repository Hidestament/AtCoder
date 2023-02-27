"""
C - LRUD Instructions 2
https://atcoder.jp/contests/abc291/tasks/abc291_c
"""

N = int(input())
S = str(input())

now = (0, 0)
points = set()

points.add(now)

flag = False
for s in S:
    if s == "R":
        now = (now[0] + 1, now[1])
    elif s == "L":
        now = (now[0] - 1, now[1])
    elif s == "U":
        now = (now[0], now[1] + 1)
    else:
        now = (now[0], now[1] - 1)

    if now in points:
        flag = True

    points.add(now)

print("Yes" if flag else "No")
