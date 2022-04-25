"""
B - Takahashi's Secret
https://atcoder.jp/contests/abc228/tasks/abc228_b
"""

N, X = map(int, input().split())
A = list(map(int, input().split()))

flag = [0] * N
now = X - 1
while True:
    if flag[now]:
        break
    flag[now] = 1
    now = A[now] - 1

print(sum(flag))
