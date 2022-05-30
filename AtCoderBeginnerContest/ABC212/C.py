"""
Min Difference
https://atcoder.jp/contests/abc212/tasks/abc212_c
"""
import bisect


N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split())) + [-(10**19), 10**19]
A.sort()
B.sort()

ans = 10**19
for a in A:
    ind = bisect.bisect_left(B, a)
    ans = min(ans, min(abs(a - B[ind]), abs(a - B[ind - 1])))
print(ans)
