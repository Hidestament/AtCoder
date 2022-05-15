"""
B - log2(N)
https://atcoder.jp/contests/abc215/tasks/abc215_b
"""

N = int(input())
print(N.bit_length() - 1)
