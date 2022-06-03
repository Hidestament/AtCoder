"""
C - POW
https://atcoder.jp/contests/abc205/tasks/abc205_c
"""

A, B, C = map(int, input().split())

if C % 2 == 0:  # 偶関数
    A, B = abs(A), abs(B)

if A < B:
    print("<")
elif A == B:
    print("=")
else:
    print(">")
