"""
B - Failing Grade
https://atcoder.jp/contests/abc222/tasks/abc222_b
"""

N, P = map(int, input().split())
A = list(map(int, input().split()))

s = sum(a < P for a in A)
print(s)
