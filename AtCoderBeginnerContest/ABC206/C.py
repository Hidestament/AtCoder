"""
C - Swappable
https://atcoder.jp/contests/abc206/tasks/abc206_c
"""
from collections import Counter

N = int(input())
A = list(map(int, input().split()))
cnt = Counter(A)

ans = sum((N - cnt[A[i]]) for i in range(N))
print(ans // 2)
