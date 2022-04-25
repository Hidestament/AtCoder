"""
C - Final Day
https://atcoder.jp/contests/abc228/tasks/abc228_c
"""

N, K = map(int, input().split())
P = [list(map(int, input().split())) for _ in range(N)]

now_points = [sum(P[i]) for i in range(N)]
base_line = sorted(now_points, reverse=True)[K - 1]

for p in now_points:
    print("Yes" if p + 300 >= base_line else "No")
