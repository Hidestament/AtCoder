"""
B - At Most 3 (Judge ver.)
https://atcoder.jp/contests/abc251/tasks/abc251_b
番兵入れると楽
"""
from itertools import combinations

N, W = map(int, input().split())
A = list(map(int, input().split())) + [0, 0]

weight = set()
for comb in combinations(range(N + 2), r=3):
    w = sum(A[i] for i in comb)
    if w <= W:
        weight.add(w)

print(len(weight))
