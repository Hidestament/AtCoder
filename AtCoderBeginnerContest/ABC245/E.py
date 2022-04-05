"""
E - Wrapping Chocolate
問題リンク: https://atcoder.jp/contests/abc245/tasks/abc245_e
座圧 + BIT (Multiset)
"""

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
D = list(map(int, input().split()))

choco = sorted([list(x) for x in zip(A, B)], key=lambda x: (-x[0], -x[1]))
box = sorted([list(x) for x in zip(C, D)], key=lambda x: (-x[0], -x[1]))


def compress(A):
    B = sorted(set(A))
    zipped = {}
    unzipped = {}
    for i, x in enumerate(B):
        zipped[x] = i
        unzipped[i] = x
    return zipped, unzipped


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


# 使える箱は, bitにwidthだけ記録していく
n = 10**6
bit = BinaryIndexedTree(n)
zipped, unzippd = compress([0] + B + D)

j, flag = 0, True
for a, b in choco:
    b = zipped[b]

    # 使える箱の更新
    while (j < M) and (box[j][0] >= a):
        bit.update(zipped[box[j][1]], 1)
        j += 1

    # 使える箱の中で, widthが最小のモノを取得する

    # widthがbより大きいモノが存在しない場合
    if bit.sum(n - 1) - bit.sum(b - 1) == 0:
        flag = False
        break

    # ちょうど width = b となる箱が存在する場合
    if bit.sum(b) - bit.sum(b - 1) > 0:
        bit.update(b, -1)
    # そうでない場合
    else:
        sum_x = bit.sum(b)
        sum_x += 1
        box_width = bit.lower_bound(sum_x)
        bit.update(box_width, -1)

print("Yes" if flag else "No")
