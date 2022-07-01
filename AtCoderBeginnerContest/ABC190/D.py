"""
D - Staircase Sequences
https://atcoder.jp/contests/abc190/tasks/abc190_d
"""

N = int(input())


def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)

    divisors.sort()
    return divisors


divisors = make_divisors(2 * N)
cnt = 0
for n in divisors:
    two_a = (2 * N) // n - n + 1
    if two_a % 2 != 0:
        continue
    cnt += 1

print(cnt)
