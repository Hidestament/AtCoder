"""
A - Alloy
https://atcoder.jp/contests/abc212/tasks/abc212_a
"""

A, B = map(int, input().split())
if 0 < A and B == 0:
    print("Gold")
elif A == 0 and 0 < B:
    print("Silver")
else:
    print("Alloy")
