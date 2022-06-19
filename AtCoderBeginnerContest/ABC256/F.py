"""
E - Takahashi's Anguish
https://atcoder.jp/contests/abc256/tasks/abc256_e
参考: https://atcoder.jp/contests/abc256/editorial/4135
"""

N, Q = map(int, input().split())
A = list(map(int, input().split()))
MOD = 998244353
two_reverse = 499122177


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
        return self.sum(j) - self.sum(i - 1)


bit1 = BinaryIndexedTree()
bit2 = BinaryIndexedTree()
bit3 = BinaryIndexedTree()

for i, a in enumerate(A, start=1):
    bit1.update(i, a)
    bit2.update(i, i * a)
    bit3.update(i, i * i * a)


for _ in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 1:
        (x, v) = q[1:]
        bit1.update(x, v - bit1.sum_range(x, x))
        bit2.update(x, x * v - bit2.sum_range(x, x))
        bit3.update(x, x * x * v - bit3.sum_range(x, x))
    else:
        x = q[1]
        ans = ((x + 1) * (x + 2) * bit1.sum(x)) % MOD
        ans -= (2 * x + 3) * bit2.sum(x)
        ans += bit3.sum(x)
        ans *= two_reverse
        print(ans % MOD)
