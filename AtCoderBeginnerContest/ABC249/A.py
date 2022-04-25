"""
A - Jogging
https://atcoder.jp/contests/abc249/tasks/abc249_a
"""

A, B, C, D, E, F, X = map(int, input().split())

num_takahashi = X // (A + C)
num_aoki = X // (D + F)

res_takahashi = min(A, X % (A+C))
res_aoki = min(D, X % (D+F))

takahashi = (A*B) * num_takahashi + (res_takahashi * B)
aoki = (D*E) * num_aoki + (res_aoki * E)

if takahashi == aoki:
    print("Draw")
elif takahashi > aoki:
    print("Takahashi")
else:
    print("Aoki")
