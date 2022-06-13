"""
D - ±1 Operation 2
https://atcoder.jp/contests/abc255/tasks/abc255_d
"""
from itertools import accumulate
from bisect import bisect_left


N, Q = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

acc = list(accumulate(A))

for _ in range(Q):
    x = int(input())
    ind = bisect_left(A, x)
    if ind == 0:
        s = acc[-1] - N * x
    elif ind == N:
        s = N * x - acc[-1]
    else:
        s = ind * x - acc[ind - 1]
        s += (acc[-1] - acc[ind - 1]) - (N - ind) * x

    print(s)
