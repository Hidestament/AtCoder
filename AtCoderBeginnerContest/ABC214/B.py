"""
B - How many?
https://atcoder.jp/contests/abc214/tasks/abc214_b
"""
from itertools import product

S, T = map(int, input().split())
cnt = 0
for a, b, c in product(range(101), range(101), range(101)):
    if (a + b + c <= S) and (a * b * c <= T):
        cnt += 1
print(cnt)
