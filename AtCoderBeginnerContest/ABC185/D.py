"""
D - Stamp
https://atcoder.jp/contests/abc185/tasks/abc185_d
"""

N, M = map(int, input().split())
A = list(map(int, input().split()))

A = [0] + sorted(A) + [N + 1]
k = 10**9
for i in range(1, M + 2):
    diff = A[i] - A[i - 1] - 1
    if diff == 0:
        continue
    k = min(k, diff)

ans = 0
for i in range(1, M + 2):
    diff = A[i] - A[i - 1] - 1
    ans += -(-diff // k)

print(ans)
