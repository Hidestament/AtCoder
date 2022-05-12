"""
A - Find Multiple
https://atcoder.jp/contests/abc220/tasks/abc220_a
"""

A, B, C = map(int, input().split())

for i in range(A, B + 1):
    if i % C == 0:
        print(i)
        exit()

print(-1)
