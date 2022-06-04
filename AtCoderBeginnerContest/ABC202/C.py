"""
C - Made Up
https://atcoder.jp/contests/abc202/tasks/abc202_c
"""
from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

cnt = defaultdict(int)
for j in range(N):
    c = C[j] - 1
    cnt[B[c]] += 1

ans = sum(cnt[a] for a in A)
print(ans)
