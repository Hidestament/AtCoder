"""
C - ±1 Operation 1
https://atcoder.jp/contests/abc255/tasks/abc255_c
"""

X, A, D, N = map(int, input().split())

if D < 0:
    A = A + D * (N - 1)
    D *= -1

a_start = A
a_end = A + D * (N - 1)

if X <= a_start:
    print(a_start - X)
    exit()

if a_end <= X:
    print(X - a_end)
    exit()

if (X - A) % D == 0:
    print(0)
    exit()

near_n = -(-(X - A) // D)
a1 = A + D * near_n
a2 = A + D * (near_n - 1)
a3 = A + D * (near_n + 1)
ans = min(abs(X - a1), abs(X - a2), abs(X - a3))

print(ans)
