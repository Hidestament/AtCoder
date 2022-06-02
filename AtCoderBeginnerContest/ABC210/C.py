"""
C - Colorful Candies
https://atcoder.jp/contests/abc210/tasks/abc210_c
"""
from collections import deque, defaultdict

N, K = map(int, input().split())
C = list(map(int, input().split()))

cnt = defaultdict(int)
dq = deque()
num_candies = 0
ans = 0
for c in C:
    dq.append(c)
    if cnt[c] == 0:
        num_candies += 1
    cnt[c] += 1
    while dq and len(dq) > K:
        rm = dq.popleft()
        if cnt[rm] == 1:
            num_candies -= 1
        cnt[rm] -= 1
    ans = max(ans, num_candies)

print(ans)
