"""
A - Swap Odd and Even
https://atcoder.jp/contests/abc293/tasks/abc293_a
"""

S = list(input())

for i in range(0, len(S), 2):
    S[i], S[i + 1] = S[i + 1], S[i]

print("".join(S))
