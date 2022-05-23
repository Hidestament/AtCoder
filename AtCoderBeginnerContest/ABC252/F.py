"""
F - Bread
https://atcoder.jp/contests/abc252/tasks/abc252_f
"""
from heapq import heapify, heappop, heappush

N, L = map(int, input().split())
A = list(map(int, input().split()))

heapify(A)
res = L - sum(A)
if res > 0:
    heappush(A, res)

cost = 0
while True:
    a1 = heappop(A)
    a2 = heappop(A)
    cost += a1 + a2
    if a1 + a2 == L:
        break
    heappush(A, a1 + a2)

print(cost)
