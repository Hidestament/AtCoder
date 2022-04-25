"""
A - First Grid
https://atcoder.jp/contests/abc229/tasks/abc229_a
"""

S1 = str(input())
S2 = str(input())

if (S1 == "#.") and (S2 == ".#"):
    print("No")
elif (S1 == ".#") and (S2 == "#."):
    print("No")
else:
    print("Yes")
