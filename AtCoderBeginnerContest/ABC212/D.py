"""
D - Querying Multiset
https://atcoder.jp/contests/abc212/tasks/abc212_d
"""
from heapq import heappush, heappop

Q = int(input())
hq = []
offset = 0

for _ in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 1:
        heappush(hq, q[1] - offset)
    elif q[0] == 2:
        offset += q[1]
    else:
        rm = heappop(hq)
        print(offset + rm)
