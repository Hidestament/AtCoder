"""
A - T-shirt
問題リンク: https://atcoder.jp/contests/abc242/tasks/abc242_a
"""

A, B, C, X = map(int, input().split())

if X <= A:
    print(1)
elif A+1 <= X <= B:
    all_num = (B - (A+1) + 1)
    print(C / all_num)
else:
    print(0)
