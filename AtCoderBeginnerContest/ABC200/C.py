"""
C - Ringo's Favorite Numbers 2
https://atcoder.jp/contests/abc200/tasks/abc200_c
"""
from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))

cnt = defaultdict(int)
for i in range(N):
    res = A[i] % 200
    cnt[res] += 1

ans = 0
for i in range(N):
    res = A[i] % 200
    ans += cnt[res] - 1
print(ans // 2)
