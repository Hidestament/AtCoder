"""
B - Climbing Takahashi
https://atcoder.jp/contests/abc235/tasks/abc235_b
"""

N = int(input())
H = list(map(int, input().split()))

now = 0
while (now < N - 1) and (H[now] < H[now+1]):
    now += 1
print(H[now])
