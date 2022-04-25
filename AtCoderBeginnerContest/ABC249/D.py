"""
D - Index Trio
https://atcoder.jp/contests/abc249/tasks/abc249_d
"""

from collections import Counter


def make_divisors(n):
    global ans, cnt
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower = i
            upper = n // i
            if lower == upper:
                ans += cnt[lower] * cnt[lower]
            else:
                ans += 2 * cnt[lower] * cnt[upper]
        i += 1


N = int(input())
A = list(map(int, input().split()))
cnt = Counter(A)

ans = 0
for i in range(N):
    make_divisors(A[i])

print(ans)
