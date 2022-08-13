"""
B - Ancestor
https://atcoder.jp/contests/abc263/tasks/abc263_b
"""

N = int(input())
P = [-1, -1] + list(map(int, input().split()))

now = N
cnt = 0
while now != 1:
    now = P[now]
    cnt += 1

print(cnt)
