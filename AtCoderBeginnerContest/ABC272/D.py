"""
D - Root M Leaper
https://atcoder.jp/contests/abc272/tasks/abc272_d
"""
import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

sqrt_nums = set([i**2 for i in range(N + 1)])

dq = deque()
dq.append([0, 0, 0])

dist = [[-1] * N for _ in range(N)]
while dq:
    i, j, d = dq.popleft()
    if dist[i][j] != -1:
        continue

    dist[i][j] = d

    for k in range(N):
        ll = M - (k - i) ** 2

        if ll not in sqrt_nums:
            continue

        l_positive = int(ll**0.5) + j
        l_negative = -1 * int(ll**0.5) + j

        if 0 <= l_positive < N:
            if dist[k][l_positive] == -1:
                dq.append([k, l_positive, d + 1])

        if 0 <= l_negative < N:
            if dist[k][l_negative] == -1:
                dq.append([k, l_negative, d + 1])

for d in dist:
    print(*d)
