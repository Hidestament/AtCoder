"""
A - Round decimals
https://atcoder.jp/contests/abc226/tasks/abc226_a
"""

X = str(input())
if int(X[-3]) >= 5:
    print(int(X[:-4]) + 1)
else:
    print(int(X[:-4]))
