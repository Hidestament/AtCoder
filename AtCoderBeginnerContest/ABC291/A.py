"""
A - camel Case
https://atcoder.jp/contests/abc291/tasks/abc291_a
"""

S = str(input())
for i, s in enumerate(S, start=1):
    if s.isupper():
        print(i)
