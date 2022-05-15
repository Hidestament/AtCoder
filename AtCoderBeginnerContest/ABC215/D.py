"""
D - Coprime 2
https://atcoder.jp/contests/abc215/tasks/abc215_d
"""

N, M = map(int, input().split())
A = list(map(int, input().split()))


divisors = set()


def make_divisors(n):
    i = 1
    while i * i <= n:
        if n % i == 0:
            divisors.add(i)
            if i != n // i:
                divisors.add(n // i)
        i += 1


for a in A:
    make_divisors(a)
divisors.remove(1)

ans = [True] * (M + 1)
ans[0] = False


for i in sorted(divisors):
    for j in range(i, M + 1, i):
        ans[j] = False

cnt = sum(ans[i] for i in range(M + 1))
print(cnt)
for i in range(M + 1):
    if ans[i]:
        print(i)
