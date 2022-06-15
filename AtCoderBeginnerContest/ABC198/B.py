"""
B - Palindrome with leading zeros
https://atcoder.jp/contests/abc198/tasks/abc198_b
"""

N = str(input())
N = int(N[::-1])
N = str(N)

print("Yes" if N == N[::-1] else "No")
