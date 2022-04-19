"""
C - Product
https://atcoder.jp/contests/abc233/tasks/abc233_c
"""

from itertools import product


N, X = map(int, input().split())
L, A = [], []
for _ in range(N):
    l, *a = map(int, input().split())
    L.append(range(l))
    A.append(a)

ans = 0
for choice in product(*L):
    prod = 1
    for i in range(N):
        select_i = choice[i]
        prod *= A[i][select_i]

    if prod == X:
        ans += 1

print(ans)
