"""
A - Lacked Number
https://atcoder.jp/contests/abc248/tasks/abc248_a
"""

S = str(input())
for i in range(10):
    if str(i) not in S:
        print(i)
