"""
A - A Recursive Function
https://atcoder.jp/contests/abc273/tasks/abc273_a
"""
import sys

input = sys.stdin.readline

N = int(input())


def f(k):
    if k == 0:
        return 1
    return k * f(k - 1)


print(f(N))
