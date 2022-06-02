"""
C - Fair Candy Distribution
https://atcoder.jp/contests/abc208/tasks/abc208_c
"""

N, K = map(int, input().split())
A = list(map(int, input().split()))

offset = K // N
K %= N

num_candy = [offset] * N
A = sorted([[a, i] for i, a in enumerate(A)])
for a, i in A:
    if K == 0:
        break
    num_candy[i] += 1
    K -= 1

print(*num_candy)
