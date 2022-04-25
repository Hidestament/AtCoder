"""
D - Project Planning
https://atcoder.jp/contests/abc227/tasks/abc227_d
"""

N, K = map(int, input().split())
A = list(map(int, input().split()))


def check(P):
    s = sum(min(a, P) for a in A)
    return s >= P * K


left, right = 0, 10**19
while (right - left) > 1:
    mid = (left + right) // 2
    if check(mid):
        left = mid
    else:
        right = mid
print(left)
