"""
A - Rock-paper-scissors
https://atcoder.jp/contests/abc204/tasks/abc204_a
"""

x, y = map(int, input().split())
print(x if x == y else 3 ^ x ^ y)
