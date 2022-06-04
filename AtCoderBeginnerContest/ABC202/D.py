"""
D - aab aba baa
https://atcoder.jp/contests/abc202/tasks/abc202_d
"""
from scipy.special import comb

A, B, K = map(int, input().split())


def dfs(a, b, k):
    if (a == 0) and (b == 0):
        print()
        return
    if a == 0:
        print("b" * b)
        return
    if b == 0:
        print("a" * a)
        return
    # a ~ となるモノの個数
    a_num = comb(a + b - 1, a - 1, exact=True)
    if k <= a_num:
        print("a", end="")
        dfs(a - 1, b, k)
    else:
        print("b", end="")
        dfs(a, b - 1, k - a_num)


dfs(A, B, K)
