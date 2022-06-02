"""
B - Can you buy them all?
https://atcoder.jp/contests/abc209/tasks/abc209_b
"""
N, X = map(int, input().split())
A = list(map(int, input().split()))

s = sum(a - (i % 2 == 1) for i, a in enumerate(A))
print("Yes" if s <= X else "No")
