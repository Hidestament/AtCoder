"""
D - Sum of difference
https://atcoder.jp/contests/abc186/tasks/abc186_d
"""

from itertools import accumulate


N = int(input())
A = sorted(list(map(int, input().split())))

acc = list(accumulate(A))

ans = 0
for i in range(N - 1):
    ans += (acc[-1] - acc[i]) - (N - i - 1) * A[i]

print(ans)
