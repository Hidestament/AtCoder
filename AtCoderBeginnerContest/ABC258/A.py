"""
A - When?
https://atcoder.jp/contests/abc258/tasks/abc258_a
"""

K = int(input())

hh = 21 + (K // 60)
mm = K % 60

print(f"{hh:02}:{mm:02}")
