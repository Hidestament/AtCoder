"""
B - Orthogonality
https://atcoder.jp/contests/abc188/tasks/abc188_b
"""

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

s = sum(A[i] * B[i] for i in range(N))
print("Yes" if s == 0 else "No")
