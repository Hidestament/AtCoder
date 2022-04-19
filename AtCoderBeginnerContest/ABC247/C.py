"""
C - 1 2 1 3 1 2 1
https://atcoder.jp/contests/abc247/tasks/abc247_c
"""


def S(n):
    if n == 1:
        return str(n)
    return S(n - 1) + " " + str(n) + " " + S(n - 1)


N = int(input())
print(S(N))
