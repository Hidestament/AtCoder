"""
A - Very Very Primitive Game
https://atcoder.jp/contests/abc190/tasks/abc190_a
"""

A, B, C = map(int, input().split())

A += C
print("Takahashi" if B < A else "Aoki")
