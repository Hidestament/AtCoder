"""
A - Vanishing Pitch
https://atcoder.jp/contests/abc191/tasks/abc191_a
"""

V, T, S, D = map(int, input().split())
print("No" if T * V <= D <= S * V else "Yes")
