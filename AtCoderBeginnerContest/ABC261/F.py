"""
F - Programming Contest
https://atcoder.jp/contests/abc184/tasks/abc184_f
参考: https://kyo-pro.hatenablog.com/entry/ABC261F
"""


from collections import defaultdict


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


N = int(input())
C = list(map(int, input().split()))
X = list(map(int, input().split()))

# 通常の転倒数を求める
bit = BinaryIndexedTree()
inversion_num = 0
for i, x in enumerate(X, start=1):
    bit.update(x, 1)
    inversion_num += i - bit.sum(x)


# 色ごとに分割する
color_x = defaultdict(list)
for c, x in zip(C, X):
    color_x[c].append(x)

# 同じ色の分の転倒数を減らす
bit = BinaryIndexedTree()
for color in color_x.values():
    for i, x in enumerate(color, start=1):
        bit.update(x, 1)
        inversion_num -= i - bit.sum(x)

    for x in color:
        bit.update(x, -1)


print(inversion_num)
