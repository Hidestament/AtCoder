"""
C - The Kth Time Query
https://atcoder.jp/contests/abc235/tasks/abc235_c
"""

from collections import defaultdict


N, Q = map(int, input().split())
A = list(map(int, input().split()))

cnt = defaultdict(list)
for i, a in enumerate(A):
    cnt[a].append(i + 1)

for _ in range(Q):
    x, k = map(int, input().split())
    if k <= len(cnt[x]):
        print(cnt[x][k-1])
    else:
        print(-1)
