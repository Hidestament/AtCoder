"""
B - Intersection
https://atcoder.jp/contests/abc199/tasks/abc199_b
"""
from itertools import accumulate


N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

imos = [0] * 1500
for a, b in zip(A, B):
    imos[a] += 1
    imos[b + 1] -= 1
imos = list(accumulate(imos))
print(imos.count(N))
