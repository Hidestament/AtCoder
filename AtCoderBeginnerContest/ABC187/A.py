"""
A - Large Digits
https://atcoder.jp/contests/abc187/tasks/abc187_a
"""

A, B = map(int, input().split())


SA = 0
for s in str(A):
    SA += int(s)

SB = 0
for s in str(B):
    SB += int(s)


print(max(SA, SB))
