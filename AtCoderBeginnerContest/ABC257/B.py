"""
B - 1D Pawn
https://atcoder.jp/contests/abc257/tasks/abc257_b
"""

N, K, Q = map(int, input().split())
A = list(map(int, input().split()))
L = list(map(int, input().split()))

A = [0] + A + [N + 1]
for mas in L:
    if A[mas] + 1 == A[mas + 1]:
        continue
    A[mas] += 1

print(*A[1:-1])
