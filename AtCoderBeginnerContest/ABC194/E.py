"""
E - Mex Min
https://atcoder.jp/contests/abc194/tasks/abc194_e
"""
from collections import defaultdict, deque
from heapq import heappush, heappop, heapify


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


def solve_bit():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))

    bit = BinaryIndexedTree(N + 2000)
    for i in range(N + 1000):
        bit.update(i, 1)

    counter = defaultdict(int)
    dq = deque()
    ans = 10**15
    for a in A:
        counter[a] += 1
        if counter[a] == 1:
            bit.update(a, -1)
        dq.append(a)
        while dq and len(dq) > M:
            rm = dq.popleft()
            if counter[rm] == 1:
                bit.update(rm, 1)
                counter[rm] = 0

        if len(dq) == M:
            ans = min(ans, bit.lower_bound(1))

    print(ans)


def solve_heapq():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))

    hq = [i for i in range(N + 10)]
    heapify(hq)
    counter = defaultdict(int)
    dq = deque()
    ans = 10**15
    for a in A:
        dq.append(a)
        counter[a] += 1

        while dq and len(dq) > M:
            rm = dq.popleft()
            counter[rm] -= 1
            if counter[rm] == 0:
                heappush(hq, rm)

        if len(dq) == M:
            while counter[hq[0]] != 0:
                heappop(hq)
            ans = min(ans, hq[0])

    print(ans)


# solve_bit()
solve_heapq()
