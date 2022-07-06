"""
E - Throne
https://atcoder.jp/contests/abc186/tasks/abc186_e
"""


from math import gcd


def solve_linear_congruential_equation(a: int, b: int, m: int):
    """Solve Linear Congruential Equation.

    solve ax = b (mod m)

    Returns:
        int: もし解が存在しなければ -1. そうでなければ最小の解xを返す.
    """
    g = gcd(a, m)
    if g == 1:
        x = b * pow(a, -1, m)
        return x % m
    elif b % g == 0:
        return solve_linear_congruential_equation(a // g, b // g, m // g)
    else:
        return -1


T = int(input())

for _ in range(T):
    N, S, K = map(int, input().split())
    print(solve_linear_congruential_equation(K, -S, N))
