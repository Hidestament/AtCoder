"""
A - Not Overflow
https://atcoder.jp/contests/abc237/tasks/abc237_a
"""

N = int(input())
print("Yes" if -pow(2, 31) <= N < pow(2, 31) else "No")
