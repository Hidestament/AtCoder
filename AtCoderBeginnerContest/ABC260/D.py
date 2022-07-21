"""
D - Draw Your Cards
https://atcoder.jp/contests/abc260/tasks/abc260_d
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

# 表向きのカードで一番上にあるモノを管理
bit = BinaryIndexedTree()
# group[top] = list[card]: topと同じグループのカードのリスト
group = {}

ans = [-1] * (N + 1)
for i, p in enumerate(P, start=1):
    # 表向きカードの更新
    all_sum = bit.sum(10**6 - 1)
    to_p_sum = bit.sum(p)

    # pより大きい数字がない場合
    if all_sum == to_p_sum:
        bit.update(p, 1)
        group[p] = [p]
    else:
        old_top = bit.lower_bound(to_p_sum + 1)
        rm = group.pop(old_top)
        rm.append(p)
        group[p] = rm
        bit.update(old_top, -1)
        bit.update(p, 1)

    # カードを食べる更新 (topは必ずp)
    if len(group[p]) == K:
        cards = group.pop(p)
        for card in cards:
            ans[card] = i
        bit.update(p, -1)


print(*ans[1:])
