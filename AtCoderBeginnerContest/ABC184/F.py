"""
F - Programming Contest
https://atcoder.jp/contests/abc184/tasks/abc184_f
"""

from bisect import bisect_right


N, T = map(int, input().split())
A = list(map(int, input().split()))

left_n = N // 2
right_n = N - left_n

left_A = A[:left_n]
right_A = A[left_n:]

right_all_sum_pattern = []
for bit in range(1 << right_n):
    s = 0
    for i in range(right_n):
        if bit & (1 << i):
            s += right_A[i]
    right_all_sum_pattern.append(s)

right_all_sum_pattern = sorted(set(right_all_sum_pattern))

ans = 0
for bit in range(1 << left_n):
    s = 0
    for i in range(left_n):
        if bit & (1 << i):
            s += left_A[i]

    if s > T:
        continue

    res = T - s
    ind = bisect_right(right_all_sum_pattern, res)
    ans = max(ans, s + right_all_sum_pattern[ind - 1])

print(ans)
