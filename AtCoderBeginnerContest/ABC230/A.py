"""
A - AtCoder Quiz 3
https://atcoder.jp/contests/abc230/tasks/abc230_a
"""

N = int(input())

if N >= 42:
    N += 1

print("AGC" + str(N).zfill(3))
