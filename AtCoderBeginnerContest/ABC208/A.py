"""
A - Rolling Dice
https://atcoder.jp/contests/abc208/tasks/abc208_a
"""
A, B = map(int, input().split())
print("Yes" if A <= B <= 6 * A else "No")
