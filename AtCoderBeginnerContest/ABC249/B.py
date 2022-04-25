"""
B - Perfect String
https://atcoder.jp/contests/abc249/tasks/abc249_b
"""

from collections import Counter

S = str(input())
cnt = Counter(S)

flag1, flag2 = False, False
for s in S:
    if s.islower():
        flag2 = True
    if s.isupper():
        flag1 = True
flag3 = all(value == 1 for _, value in cnt.items())

print("Yes" if flag1 and flag2 and flag3 else "No")
