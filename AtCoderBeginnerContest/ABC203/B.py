"""
B - AtCoder Condominium
https://atcoder.jp/contests/abc203/tasks/abc203_b
"""
from itertools import product

N, K = map(int, input().split())

s = 0
for i, j in product(range(1, N + 1), range(1, K + 1)):
    s += 100 * i + j
print(s)
