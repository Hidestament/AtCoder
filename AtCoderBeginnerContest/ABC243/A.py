"""
A - Shampoo
問題リンク: https://atcoder.jp/contests/abc243/tasks/abc243_a
"""

V, A, B, C = map(int, input().split())

V %= (A + B + C)

if V - A < 0:
    print("F")
elif V - (A + B) < 0:
    print("M")
else:
    print("T")
