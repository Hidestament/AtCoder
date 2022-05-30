"""
F - Operations on a Matrix
https://atcoder.jp/contests/abc253/tasks/abc253_f
"""
from collections import deque, defaultdict


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


N, M, Q = map(int, input().split())

bit = BinaryIndexedTree()

# last_update_time[t] = [t1, t2, ...]: 時間tが最後のupdateとなるクエリ3のリスト
last_update_time = defaultdict(list)
queries = [[2, 0, 0]]
two_queries = [deque([[0, 2, 0, 0]]) for _ in range(N + 1)]
for t in range(1, Q + 1):
    q = list(map(int, input().split()))
    if q[0] == 2:
        two_queries[q[1]].append([t] + q)
    elif q[0] == 3:
        last_time = two_queries[q[1]][-1][0]
        last_update_time[last_time].append(t)
    queries.append(q)

last_update_value = [0] * (Q + 1)
for t, q in enumerate(queries):
    if q[0] == 1:
        (_, l, r, x) = q
        bit.update(l, x)
        bit.update(r + 1, -x)
    elif q[0] == 2:
        # このクエリー時点でのj列目の値を記録
        for dt in last_update_time[t]:
            (_, i, j) = queries[dt]
            last_update_time[dt] = [bit.sum(j), q[2]]
    else:
        (_, i, j) = q
        (before_update, update_value) = last_update_time[t]
        now_value = bit.sum(j)
        print(now_value - before_update + update_value)
