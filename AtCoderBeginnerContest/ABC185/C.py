"""
C - Duodecim Ferra
https://atcoder.jp/contests/abc185/tasks/abc185_c
"""

from scipy.special import comb


L = int(input())
print(comb(L - 1, 11, exact=True))
