"""
C - Happy New Year!
https://atcoder.jp/contests/abc234/tasks/abc234_c
"""

K = int(input())

ans = bin(K)[2:]
ans = ans.replace("1", "2")
print(ans)
