"""
A - Last Card
https://atcoder.jp/contests/abc227/tasks/abc227_a
"""

N, K, A = map(int, input().split())

# 0-index
A -= 1
print((A + (K - 1)) % N + 1)
