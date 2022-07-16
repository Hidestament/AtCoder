"""
E - LCM on Whiteboard
https://atcoder.jp/contests/abc259/tasks/abc259_e
参考: https://www.youtube.com/watch?v=8pv0U8-Oe-Y
"""

from collections import defaultdict


N = int(input())

lcm = defaultdict(int)
primes = [[] for _ in range(N)]
for i in range(N):
    m = int(input())
    for _ in range(m):
        p, e = map(int, input().split())
        lcm[p] = max(lcm[p], e)
        primes[i].append([p, e])

max_cnt = defaultdict(int)
for i in range(N):
    for p, e in primes[i]:
        if lcm[p] == e:
            max_cnt[p] += 1

ans = 0
for i in range(N):
    flag = False
    for p, e in primes[i]:
        if (lcm[p] == e) and (max_cnt[p] == 1):
            flag = True
    if flag:
        ans += 1

if ans < N:
    ans += 1

print(ans)
