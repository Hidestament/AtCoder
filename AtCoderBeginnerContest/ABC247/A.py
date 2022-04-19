"""
A - Move Right
https://atcoder.jp/contests/abc247/tasks/abc247_a
"""

S = int(str(input()), 2)
S = S >> 1
S = bin(S)[2:]
S = S.zfill(4)  # 0埋め

print(S)
