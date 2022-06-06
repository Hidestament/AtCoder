"""
C - Secret Number
https://atcoder.jp/contests/abc201/tasks/abc201_c
"""
from itertools import product

S = str(input())

maru_list = sorted([i for i in range(10) if S[i] == "o"])
batu_set = set([i for i in range(10) if S[i] == "x"])

cnt = 0
for a1, a2, a3, a4 in product(range(10), range(10), range(10), range(10)):
    if not all(a in set([a1, a2, a3, a4]) for a in maru_list):
        continue
    if all(a not in batu_set for a in [a1, a2, a3, a4]):
        cnt += 1

print(cnt)
