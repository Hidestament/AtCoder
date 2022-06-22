"""
B - Remove It
https://atcoder.jp/contests/abc191/tasks/abc191_b
"""

N, X = map(int, input().split())
A = list(map(int, input().split()))

A = [a for a in A if a != X]
print(*A)
