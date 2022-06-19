"""
D - Union of Interval
https://atcoder.jp/contests/abc256/tasks/abc256_d
"""
from itertools import accumulate

N = int(input())
imos = [0] * (10**6)

for _ in range(N):
    l, r = map(int, input().split())
    imos[l] += 1
    imos[r] -= 1

imos = list(accumulate(imos))

flag = False
for i, value in enumerate(imos):
    if (not flag) and value > 0:
        left = i
        flag = True
    elif flag and value == 0:
        right = i
        flag = False
        print(left, right)
