"""
C - digitnum
https://atcoder.jp/contests/abc238/tasks/abc238_c
"""

N = int(input())
dig = len(str(N))
mod = 998244353


def tousa_sum(n):
    """初項1, 項数n, 公差1の等差数列の和
    """
    return n * (n + 1) // 2


# Nが一桁のときは, 場合分けして解いてしまう
if dig == 1:
    print(tousa_sum(N))
    exit()


ans = 0
for k in range(1, dig+1):
    if k == 1:
        n = 9 - 1 + 1
    elif k == dig:
        n = N - 10**(k-1) + 1
    else:
        n = 10**k - 10**(k-1)

    ans += tousa_sum(n)
    ans %= mod

print(ans)
