"""
D - Three Days Ago
https://atcoder.jp/contests/abc295/tasks/abc295_d
"""
import sys
from collections import Counter

input = sys.stdin.readline

S = input().split()[0]

num_bits = [0]
now = 0
for s in S:
    number = int(s)
    now = now ^ (1 << number)
    num_bits.append(now)

cnt = Counter(num_bits)
ans = 0
for bit in num_bits:
    cnt[bit] -= 1
    ans += cnt[bit]

print(ans)
