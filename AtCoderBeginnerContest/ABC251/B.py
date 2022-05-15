"""
B - At Most 3 (Judge ver.)
https://atcoder.jp/contests/abc251/tasks/abc251_b
"""
from itertools import combinations

N, W = map(int, input().split())
A = list(map(int, input().split()))

weight = set()
for r in range(1, 4):
    for comb in combinations(range(N), r=r):
        w = sum(A[i] for i in comb)
        if w <= W:
            weight.add(w)

print(len(weight))
