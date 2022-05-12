"""
C - Long Sequence
https://atcoder.jp/contests/abc220/tasks/abc220_c
"""
N = int(input())
A = list(map(int, input().split()))
X = int(input())

s = sum(A)
ans = N * (X // s)
X %= s
for i in range(N):
    X -= A[i]
    ans += 1
    if X < 0:
        print(ans)
        break
