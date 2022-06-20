"""
B - Job Assignment
https://atcoder.jp/contests/abc194/tasks/abc194_b
"""
from itertools import product

N = int(input())
A, B = zip(*[list(map(int, input().split())) for _ in range(N)])

ans = 10**15
for i, j in product(range(N), range(N)):
    if i == j:
        work_time = A[i] + B[j]
    else:
        work_time = max(A[i], B[j])

    ans = min(ans, work_time)

print(ans)
