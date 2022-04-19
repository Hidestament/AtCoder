"""
D - Cylinder
https://atcoder.jp/contests/abc247/tasks/abc247_d
"""

from collections import deque


Q = int(input())

dq = deque()
for _ in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 1:
        dq.append([q[1], q[2]])
    else:
        c = q[1]
        s, cnt = 0, 0
        while cnt < c:
            nx, nc = dq[0]
            if cnt + nc > c:
                res = c - cnt
                s += nx * res
                dq[0][1] -= res
                break
            else:
                dq.popleft()
                cnt += nc
                s += nx * nc
        print(s)
