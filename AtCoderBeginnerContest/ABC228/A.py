"""
A - On and Off
https://atcoder.jp/contests/abc228/tasks/abc228_a
"""

S, T, X = map(int, input().split())

if S <= T:
    print("Yes" if S <= X < T else "No")
else:
    print("Yes" if (S <= X) or (X < T) else "No")
