"""
A - Chinchirorin
https://atcoder.jp/contests/abc203/tasks/abc203_a
"""

a, b, c = map(int, input().split())
if a == b:
    print(c)
elif b == c:
    print(a)
elif a == c:
    print(b)
else:
    print(0)
