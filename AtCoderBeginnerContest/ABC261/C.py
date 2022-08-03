"""
C - NewFolder(1)
https://atcoder.jp/contests/abc261/tasks/abc261_c
"""

from collections import defaultdict


N = int(input())

counter = defaultdict(int)
for _ in range(N):
    s = str(input())
    if s not in counter:
        print(s)
    else:
        print(f"{s}({counter[s]})")

    counter[s] += 1
