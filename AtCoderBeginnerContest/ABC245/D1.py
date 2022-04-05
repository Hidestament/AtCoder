"""
D - Polynomial division
問題リンク: https://atcoder.jp/contests/abc245/tasks/abc245_d
numpyで解く
"""

import numpy as np

N, M = map(int, input().split())
A = list(map(int, input().split()))
C = list(map(int, input().split()))

poly_a = np.poly1d(A[::-1])
poly_c = np.poly1d(C[::-1])

poly_b = poly_c / poly_a
poly_b = list(poly_b[0].coef)[::-1]
poly_b = list(map(int, poly_b))
print(*poly_b)
