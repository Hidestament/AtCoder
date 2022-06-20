"""
C - Squared Error
https://atcoder.jp/contests/abc194/tasks/abc194_c
"""

N = int(input())
A = list(map(int, input().split()))

s = sum(A)
ans = 0
for i in range(N):
    ans += N * (A[i] ** 2)
    ans -= A[i] * s

print(ans)
