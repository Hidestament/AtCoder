"""
C - One More aab aba baa
https://atcoder.jp/contests/abc215/tasks/abc215_c
"""
from itertools import permutations

S, K = input().split()
S = sorted(set(permutations(S)))
print("".join(S[int(K) - 1]))
