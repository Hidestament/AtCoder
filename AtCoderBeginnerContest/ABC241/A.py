"""
A - Digit Machine
https://atcoder.jp/contests/abc241/tasks/abc241_a
"""

a = list(map(int, input().split()))

now = 0
for _ in range(3):
    now = a[now]

print(now)
