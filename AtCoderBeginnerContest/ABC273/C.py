"""
C - (K+1)-th Largest Number
https://atcoder.jp/contests/abc273/tasks/abc273_c
"""
import sys
from collections import defaultdict

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

sortedA = sorted(set(A), reverse=True)

# cnt[x]: xより大きいものの個数
cnt = defaultdict(int)
for i, a in enumerate(sortedA):
    cnt[a] = i

ans = [0] * N
for a in A:
    ans[cnt[a]] += 1

print(*ans)
