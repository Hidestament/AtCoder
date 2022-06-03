"""
B - Permutation Check
https://atcoder.jp/contests/abc205/tasks/abc205_b
"""

N = int(input())
A = list(map(int, input().split()))
A.sort()

print("Yes" if A == [i for i in range(1, N + 1)] else "No")
