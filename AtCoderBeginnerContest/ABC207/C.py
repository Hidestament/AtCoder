"""
C - Many Segments
https://atcoder.jp/contests/abc207/tasks/abc207_c
"""
from itertools import combinations


N = int(input())
segments = []
for _ in range(N):
    t, left, right = map(int, input().split())
    if t == 2:
        right -= 0.5
    elif t == 3:
        left += 0.5
    elif t == 4:
        left += 0.5
        right -= 0.5
    segments.append([left, right])

ans = 0
for i, j in combinations(range(N), r=2):
    l1, r1 = segments[i]
    l2, r2 = segments[j]
    ans += max(l1, l2) <= min(r1, r2)

print(ans)
