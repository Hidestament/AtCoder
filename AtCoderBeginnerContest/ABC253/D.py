"""
D - FizzBuzz Sum Hard
https://atcoder.jp/contests/abc253/tasks/abc253_d
"""
from math import gcd


def tousa_sum(a, n):
    return n * (2 * a + (n - 1) * a) // 2


N, A, B = map(int, input().split())
all_s = tousa_sum(1, N)

num_a = N // A
a = tousa_sum(A, num_a)

num_b = N // B
b = tousa_sum(B, num_b)

AB = A * B // gcd(A, B)
num_ab = N // AB
ab = tousa_sum(AB, num_ab)


print(all_s - a - b + ab)
