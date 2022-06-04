"""
B - 180°
https://atcoder.jp/contests/abc202/tasks/abc202_b
"""

S = str(input())
S = S[::-1]

S = S.replace("9", "x")
S = S.replace("6", "9")
S = S.replace("x", "6")
print(S)
