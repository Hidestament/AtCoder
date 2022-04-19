"""
D - Prefix K-th Max
https://atcoder.jp/contests/abc234/tasks/abc234_d
BITをMultisetとして使って解く
"""


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
            # 左上は i に iのLSBを引いたモノ
            pos -= pos & -pos
        return s

    def sum_range(self, i, j):
        """
        a[i] + a[i+1] + ... + a[j] を 求める
        i, j は 0-index
        """
        return self.sum(j) - self.sum(i - 1)

    def lower_bound(self, x):
        """
        a0 + a1 + ... + ai >= x となる最小のiを取得.
        各項は非負である必要がある
        iは0 - index
        """
        if x <= 0:
            return -1

        k = 1 << (self.size.bit_length() - 1)
        pos = 0
        s = 0
        while k > 0:
            # (pos + kが配列の長さを超えない) and 和がxを超えない
            if (pos + k < self.size) and self.tree[pos + k] + s < x:
                s += self.tree[pos + k]
                pos += k
            # 1つ下の段に行く
            k //= 2
        return pos


N, K = map(int, input().split())
P = list(map(int, input().split()))

n = 10**6
bit = BinaryIndexedTree(n)
for i, p in enumerate(P, start=1):
    bit.update(p, 1)
    if i >= K:
        all_s = bit.sum(n - 1)
        ans = bit.lower_bound(all_s - (K - 1))
        print(ans)
