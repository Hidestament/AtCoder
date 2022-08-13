"""
E - Sugoroku 3
https://atcoder.jp/contests/abc263/tasks/abc263_e
参考: https://atcoder.jp/contests/abc263/editorial/4552
"""

N = int(input())
A = list(map(int, input().split()))
MOD = 998244353


class BinaryIndexedTree:
    """
    A = [a0, a1, a2, ..., an-1]
    元のAの配列は0-indexだが, BIT上では1-indexで扱う
    """

    def __init__(self, n=10**6):
        self.size = n + 1
        self.tree = [0] * (n + 1)
        self.depth = n.bit_length()

    def update(self, i, x):
        """
        ai += x を する
        i: 0-index
        """
        # 1-indexに直す
        pos = i + 1
        while pos <= self.size:
            self.tree[pos] += x
            self.tree[pos] %= MOD
            # 真上の位置は, iにiのLSBを加えたモノ
            pos += pos & -pos

    def sum(self, i):
        """
        a[0] + a[1] + ... + a[i] を 求める
        i は 0-index
        """
        pos = i + 1
        s = 0
        while pos > 0:
            s += self.tree[pos]
            s %= MOD
            # 左上は i に iのLSBを引いたモノ
            pos -= pos & -pos
        return s

    def sum_range(self, i, j):
        """
        a[i] + a[i+1] + ... + a[j] を 求める
        i, j は 0-index
        """
        return (self.sum(j) - self.sum(i - 1)) % MOD


def xgcd(a, b):
    x0, y0, x1, y1 = 1, 0, 0, 1
    while b != 0:
        q, a, b = a // b, b, a % b
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return a, x0, y0


def modinv(a, m):
    g, x, y = xgcd(a, m)
    if g != 1:
        raise Exception("modular inverse does not exist")
    else:
        return x % m


# Ainv: Aの逆元
Ainv = [modinv(a, MOD) for a in A]

# DP[i]: iからNにたどり着く期待値
# 初期状態: DP[N] = 0
DP = [0] * (N + 1)

bit = BinaryIndexedTree()

s = 0
for i in range(1, N)[::-1]:
    a = A[i - 1]
    a_inv = Ainv[i - 1]
    s = bit.sum_range(i + 1, i + a)
    x = (s * a_inv + (a + 1) * a_inv) % MOD
    DP[i] = x
    bit.update(i, x)

print(DP[1])
