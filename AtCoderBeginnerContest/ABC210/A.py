"""
A - Cabbages
https://atcoder.jp/contests/abc210/tasks/abc210_a
"""
N, A, X, Y = map(int, input().split())
print(min(A, N) * X + max(0, (N - A)) * Y)
