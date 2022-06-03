"""
B - Nuts
https://atcoder.jp/contests/abc204/tasks/abc204_b
"""

N = int(input())
A = list(map(int, input().split()))

A = [max(0, a - 10) for a in A]
print(sum(A))
