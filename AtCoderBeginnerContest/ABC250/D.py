"""
D - 250-like Number
https://atcoder.jp/contests/abc250/tasks/abc250_d
"""
import math
from collections import deque


N = int(input())
upper = 2 * (10**6)


def sieve_of_eratosthenes(n=upper):
    prime = [True for i in range(n + 1)]
    prime[0] = False
    prime[1] = False

    sqrt_n = math.ceil(math.sqrt(n))
    for i in range(2, sqrt_n):
        if prime[i]:
            for j in range(2 * i, n + 1, i):
                prime[j] = False

    return [i for i in range(upper) if prime[i]]


primes = sieve_of_eratosthenes()
dq = deque()
ans = 0

for q in primes:
    q3 = pow(q, 3)
    if q3 > N:
        continue
    while dq and (dq[-1] * q3 > N):
        rm = dq.pop()
    ans += len(dq)
    dq.append(q)

print(ans)
