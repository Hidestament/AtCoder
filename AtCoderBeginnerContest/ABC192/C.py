"""
C - Kaprekar Number
https://atcoder.jp/contests/abc192/tasks/abc192_c
"""

N, K = map(int, input().split())


def g1(x):
    x = int("".join(sorted(str(x), reverse=True)))
    return x


def g2(x):
    x = int("".join(sorted(str(x))))
    return x


def f(x):
    return g1(x) - g2(x)


a = N
for _ in range(K):
    a = f(a)
print(a)
