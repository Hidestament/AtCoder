"""
E - At Least One
https://atcoder.jp/contests/abc260/tasks/abc260_e
参考: https://atcoder.jp/contests/abc260/editorial/4458
    : https://www.youtube.com/watch?v=LL4R6BU2gW8
"""

from heapq import heappush
from itertools import accumulate
from collections import defaultdict


N, M = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(N)]
A, B = map(list, zip(*AB))

A_ind = defaultdict(list)
for i, a in enumerate(A):
    A_ind[a].append(i)

B_ind = defaultdict(list)
for i, b in enumerate(B):
    B_ind[b].append(i)

max_hq = []
for a in A:
    heappush(max_hq, -a)

min_hq = []

f = [0] * (M + 2)
for left in range(1, M + 1):
    right = -max_hq[0]

    if min_hq:
        if min_hq[0] < left:
            break

    min_sequence_length = right - left + 1
    max_sequence_length = M - left + 1
    f[min_sequence_length] += 1
    f[max_sequence_length + 1] -= 1

    for i in A_ind[left]:
        heappush(max_hq, -B[i])

    for i in B_ind[left]:
        heappush(min_hq, B[i])


f = list(accumulate(f))
print(*f[1:-1])
