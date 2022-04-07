"""
F - Sum Sum Max
https://atcoder.jp/contests/abc240/tasks/abc240_f
[x, y]ごとの区間で考える. このとき
C: 定数
B: 1次関数
A: 2次関数
として表される.
参考: https://kazun-kyopro.hatenablog.com/entry/ABC/240/F
"""


def get_b(b, c, k):
    """今考えている区間のBのk番目の値を返す

    Args:
        b (int): 前の区間の最後のbの値
        c (int): 現在の区間のcの値
        k (int): k番目の値 1 <= k <= y
    """
    return b + k * c


def get_a(a, b, c, k):
    """今考えている区間のAのk番目の値を返す

    Args:
        a (int): 前の区間の最後のaの値
        b (int): 前の区間の最後のbの値
        c (int): 現在の区間のcの値
        k (int): k番目の値 1 <= k <= y
    """
    return a + k*b + (c*k*(k+1))//2


T = int(input())
for _ in range(T):
    N, M = map(int, input().split())

    C, B, A = [], [0], [0]
    ans = -10**10
    for _ in range(N):
        c, y = map(int, input().split())
        a, b = A[-1], B[-1]

        # 現在の区間の最初のaの値
        a_first = get_a(a, b, c, 1)
        # 現在の区間の最後のaの値
        a_last = get_a(a, b, c, y)

        ans = max(ans, a_first, a_last)

        # c < 0 ならAは上に凸なので, 端点以外が最大値となる場合がある
        if c < 0:
            # 極地の場所
            points = -1 * (2*B[-1] + c) // (2*c)

            # 切り捨て切り上げが面倒なので, +-1の範囲を探索
            if 1 <= points <= y:
                ans = max(ans, get_a(a, b, c, points))
            if 1 <= points-1 <= y:
                ans = max(ans, get_a(a, b, c, points-1))
            if 1 <= points+1 <= y:
                ans = max(ans, get_a(a, b, c, points+1))

        # 数列の最後の値の更新
        B.append(get_b(b, c, y))
        A.append(a_last)

    print(ans)
