"""
A - Distinct Strings
https://atcoder.jp/contests/abc225/tasks/abc225_a
"""

S = set(str(input()))

if len(S) == 1:
    print(1)
elif len(S) == 2:
    print(3)
else:
    print(6)
