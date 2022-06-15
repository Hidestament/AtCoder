"""
C - ORXOR
https://atcoder.jp/contests/abc197/tasks/abc197_c
"""

N = int(input())
A = list(map(int, input().split()))

ans = 10**20
for bit in range(1 << (N - 1)):
    a_xor = 0
    a_or = A[0]
    for i in range(N - 1):
        if bit & (1 << i):
            a_xor ^= a_or
            a_or = A[i + 1]
        else:
            a_or |= A[i + 1]
    a_xor ^= a_or
    ans = min(ans, a_xor)

print(ans)
