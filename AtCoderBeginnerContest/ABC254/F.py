"""
F - Rectangle GCD
https://atcoder.jp/contests/abc254/tasks/abc254_f
参考: https://atcoder.jp/contests/abc254/editorial/4067
"""
from math import gcd


class SegmentTree:
    """1点更新・区間集約 Segment Tree. 非再起・1-index・非可換

    Attributes:
        tree (List[Union[int, float]]): セグメントツリーを表す配列
        segfunc (Callable): 集約を行う関数 (モノイド上の演算)
        ide_ele (float): 集約の関数における単位元　（モノイド上の単位元）
        update (int, float): 元の配列の更新 & セグメントツリーの更新
        query (int, int): 区間集約値の取得
    """

    def __init__(self, n: int, ide_ele: float, seg_func: callable):
        """
        Args:
            n (int): 元の配列のサイズ
            ide_ele (float): モノイドにおける単位元
            segfunc (callable): 集約を行う関数 （モノイド上の演算）
        """
        self.segfunc = seg_func
        self.ide_ele = ide_ele
        self.num = 1 << (n - 1).bit_length()
        self.tree = [self.ide_ele] * (2 * self.num)

    def update(self, i: int, x: float) -> None:
        """元の配列のi番目を x に変更（上書き）する. それに伴ってセグメントツリーも更新する. +=のようなupdateではない.

        Args:
            i (int): 元の配列のi番目の要素. 元の配列の0-indexの
            x (float): 変更後の値
        """
        i += self.num
        self.tree[i] = x
        while i > 1:
            i >>= 1
            self.tree[i] = self.segfunc(self.tree[i << 1], self.tree[(i << 1) + 1])

    def query(self, l: int, r: int):
        """元の配列の閉区間[l, r]のsegfuncにおける集約値を取得する

        Args:
            l (int): 元の配列の集約を行う区間の左端のindex. 0-index
            r (int): 元の配列の集約を行う区間の右端のindex. 0-index
        """
        # [l, r) として葉から計算していく
        l += self.num
        r += self.num + 1

        l_res = self.ide_ele
        r_res = self.ide_ele

        while l < r:
            if l & 1:  # lが奇数だったらそのノードを集約する
                l_res = self.segfunc(l_res, self.tree[l])
                l += 1  # 右に進む
            if r & 1:  # rが奇数だったら, rは開区間なので その1つ左ノードを集約する
                r_res = self.segfunc(self.tree[r - 1], r_res)

            l >>= 1  # 上に進む（２で割って切り捨て）
            r >>= 1

        return self.segfunc(l_res, r_res)


N, Q = map(int, input().split())
A = [0] + list(map(int, input().split()))
B = [0] + list(map(int, input().split()))

A_diff = [0] + [A[i + 1] - A[i] for i in range(N)]
B_diff = [0] + [B[i + 1] - B[i] for i in range(N)]

A_seg = SegmentTree(n=10**6, ide_ele=0, seg_func=gcd)
for i, a in enumerate(A_diff):
    A_seg.update(i, a)

B_seg = SegmentTree(n=10**6, ide_ele=0, seg_func=gcd)
for j, b in enumerate(B_diff):
    B_seg.update(j, b)

for _ in range(Q):
    h1, h2, w1, w2 = map(int, input().split())
    ans = A[h1] + B[w1]
    ans = gcd(ans, A_seg.query(h1 + 1, h2))
    ans = gcd(ans, B_seg.query(w1 + 1, w2))
    print(ans)
