"""
C - Inverse of Permutation
https://atcoder.jp/contests/abc217/tasks/abc217_c
"""
N = int(input())
P = list(map(int, input().split()))

Q = [-1] * N
for i, p in enumerate(P, start=1):
    Q[p - 1] = i

print(*Q)
