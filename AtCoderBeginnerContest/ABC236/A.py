"""
A - chukodai
https://atcoder.jp/contests/abc236/tasks/abc236_a
"""

S = list(str(input()))
a, b = map(int, input().split())

S[a-1], S[b-1] = S[b-1], S[a-1]
print("".join(S))
