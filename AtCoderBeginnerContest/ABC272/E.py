"""
E - Add and Mex
https://atcoder.jp/contests/abc272/tasks/abc272_e
"""
import sys
from math import ceil

input = sys.stdin.readline

N, M = map(int, input().split())
A = list(map(int, input().split()))

used_numbers = [set() for _ in range(M)]
for i in range(1, N + 1):
    a = A[i - 1]

    min_k = max(ceil(-1 * a / i), 0)
    if min_k > M:
        continue

    max_k = min((N - a) // i, M)
    if max_k < 0:
        continue

    for k in range(min_k, max_k + 1):
        used_numbers[k - 1].add(a + i * k)


for k in range(M):
    mex = 0
    while mex in used_numbers[k]:
        mex += 1
    print(mex)
