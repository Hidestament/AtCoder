"""
B - Election
https://atcoder.jp/contests/abc231/tasks/abc231_b
"""

from collections import defaultdict


N = int(input())
cnt = defaultdict(int)
for _ in range(N):
    s = str(input())
    cnt[s] += 1

print(max(cnt, key=cnt.get))
