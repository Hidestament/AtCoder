"""
E - Sorting Queries
https://atcoder.jp/contests/abc217/tasks/abc217_e
"""
from collections import deque
from heapq import heappop, heappush


Q = int(input())
dq = deque()
hq = []
for _ in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 1:
        dq.append(q[1])
    elif q[0] == 2:
        if hq:
            rm = heappop(hq)
        else:
            rm = dq.popleft()
        print(rm)
    else:
        while dq:
            rm = dq.popleft()
            heappush(hq, rm)
