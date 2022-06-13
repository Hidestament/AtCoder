"""
F - Pre-order and In-order
https://atcoder.jp/contests/abc255/tasks/abc255_f
参考: https://atcoder.jp/contests/abc255/editorial/4105
"""
import sys

sys.setrecursionlimit(10**7)

N = int(input())
P = list(map(int, input().split()))
I = list(map(int, input().split()))

if P[0] != 1:
    print(-1)
    exit()

rI = {v: i for i, v in enumerate(I)}
Tree = [None] * (N + 1)


def dfs(Lp: int, Rp: int, Li: int, Ri: int):
    """
    Args:
        [Lp, Rp]: P[Lp:Rp+1]の区間
        [Li, Ri]: I[Li:Ri+1]の区間
    """
    if (Lp > Rp) or (Li > Ri):
        return 0

    root = P[Lp]
    i_ind = rI[root]

    if not (Li <= i_ind <= Ri):
        print(-1)
        exit()

    # 左部分木
    num_left_children = i_ind - Li
    # Pの左部分木の位置は, [Lp+1, Lp + num_left_children]
    left = dfs(Lp + 1, Lp + num_left_children, Li, i_ind - 1)

    # 右部分木
    num_right_children = Ri - i_ind
    # Pの右部分木の位置は, [Rp - num_left_children + 1, Rp]
    right = dfs(Rp - num_right_children + 1, Rp, i_ind + 1, Ri)

    Tree[root] = (left, right)
    return root


dfs(0, N - 1, 0, N - 1)
for left, right in Tree[1:]:
    print(left, right)
