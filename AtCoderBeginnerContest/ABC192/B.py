"""
B - uNrEaDaBlE sTrInG
https://atcoder.jp/contests/abc192/tasks/abc192_b
"""

S = str(input())
flag = True
for i, s in enumerate(S):
    if i % 2 == 0:
        flag &= s.islower()
    else:
        flag &= s.isupper()

print("Yes" if flag else "No")
