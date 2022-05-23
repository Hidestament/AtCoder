"""
C - Slot Strategy
https://atcoder.jp/contests/abc252/tasks/abc252_c
"""
from collections import Counter

N = int(input())
slot = [input() for _ in range(N)]

ans = 10**15
for num in range(10):
    num = str(num)
    ind = [s.index(num) for s in slot]
    cnt = Counter(ind)
    ans = min(ans, max((10 * (value - 1) + key) for key, value in cnt.items()))

print(ans)
