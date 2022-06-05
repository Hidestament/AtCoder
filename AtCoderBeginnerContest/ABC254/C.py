"""
C - K Swap
https://atcoder.jp/contests/abc254/tasks/abc254_c
"""
from itertools import zip_longest


N, K = map(int, input().split())
A = list(map(int, input().split()))

grouped_A = [sorted(A[i::K]) for i in range(K)]
sorted_A = []
for a in zip_longest(*grouped_A):
    for value in a:
        if value is not None:
            sorted_A.append(value)

print("Yes" if sorted_A == sorted(A) else "No")
