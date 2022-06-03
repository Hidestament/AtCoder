"""
D - Kth Excluded
https://atcoder.jp/contests/abc205/tasks/abc205_d
"""
from bisect import bisect_left


N, Q = map(int, input().split())
A = [0] + list(map(int, input().split())) + [10**50]

# cnt[i]: A[i]未満のAに含まれないモノの個数
cnt = [0] * (N + 2)
for i in range(1, N + 2):
    cnt[i] = cnt[i - 1] + (A[i] - A[i - 1] - 1)

for _ in range(Q):
    k = int(input())
    ind = bisect_left(cnt, k)
    k -= cnt[ind - 1]
    print(A[ind - 1] + k)
