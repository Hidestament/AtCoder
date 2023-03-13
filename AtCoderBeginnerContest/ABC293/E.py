"""
E - Geometric Progression
https://atcoder.jp/contests/abc293/tasks/abc293_e
"""
import numpy as np

A, X, M = map(int, input().split())

a = np.matrix([[A, 1], [0, 1]])

result = np.matrix([[1, 0], [0, 1]])
base = a
while X:
    if X % 2:
        result *= base

    base *= base

    base %= M
    result %= M

    X >>= 1

print(result[0, 1])
