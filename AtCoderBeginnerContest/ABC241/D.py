"""
D - Sequence Query
https://atcoder.jp/contests/abc241/tasks/abc241_d
クエリ先読み + 座圧 + BIT
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


def compress(A):
    B = sorted(set(A))
    zipped = {}
    unzipped = {}
    for i, x in enumerate(B):
        zipped[x] = i
        unzipped[i] = x
    return zipped, unzipped


Q = int(input())
queries, used = [], []
for _ in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 1:
        q.append(-1)
    queries.append(q)
    used.append(q[1])

zipped, unzipped = compress(used)

bit = BinaryIndexedTree()
for t, x, k in queries:
    x = zipped[x]
    if t == 1:
        bit.update(x, 1)

    elif t == 2:
        # x以下の要素数がいくつあるか
        num = bit.sum(x)
        if num >= k:
            ans = bit.lower_bound(num - (k-1))
            print(unzipped[ans])
        else:
            print(-1)

    else:
        # x以上の要素数がいくつあるか
        num = bit.sum_range(x, 10**6-1)
        if num >= k:
            s = bit.sum(x - 1)
            ans = bit.lower_bound(s + k)
            print(unzipped[ans])
        else:
            print(-1)
