"""
C - Socks
https://atcoder.jp/contests/abc295/tasks/abc295_c
"""
import sys
from collections import Counter

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

cnt = Counter(A)

ans = 0
for value in cnt.values():
    ans += value // 2

print(ans)
