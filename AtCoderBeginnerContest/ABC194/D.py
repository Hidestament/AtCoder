"""
D - Journey
https://atcoder.jp/contests/abc194/tasks/abc194_d
"""

N = int(input())
s = sum((1 / i) for i in range(1, N))
print(N * s)
