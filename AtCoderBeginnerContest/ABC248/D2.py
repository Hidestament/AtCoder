"""
D - Range Count Query
https://atcoder.jp/contests/abc248/tasks/abc248_d
二分探索で解く
"""

from bisect import bisect_left, bisect_right
from collections import defaultdict


N = int(input())
A = list(map(int, input().split()))

# cnt[a]: a in A の index のソートされたリスト（[2, 3, 6]的な）
cnt = defaultdict(list)
for i, a in enumerate(A, start=1):
    cnt[a].append(i)
for a in cnt:
    cnt[a] = sorted(cnt[a])

Q = int(input())
for _ in range(Q):
    left, right, x = map(int, input().split())
    ans = bisect_right(cnt[x], right) - bisect_left(cnt[x], left)
    print(ans)
