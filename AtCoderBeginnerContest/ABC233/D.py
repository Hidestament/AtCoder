"""
D - Count Interval
https://atcoder.jp/contests/abc233/tasks/abc233_d
"""

from collections import defaultdict
from itertools import accumulate


N, K = map(int, input().split())
A = list(map(int, input().split()))
acc = [0] + list(accumulate(A))

ans = 0
cnt = defaultdict(int)
for i, a in enumerate(acc[1:], start=1):
    cnt[acc[i-1]] += 1  # 使えるLの更新
    res = a - K
    ans += cnt[res]

print(ans)
