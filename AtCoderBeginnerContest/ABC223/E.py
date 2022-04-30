"""
E - Placing Rectangles
https://atcoder.jp/contests/abc223/tasks/abc223_e
参考: https://www.youtube.com/watch?v=-Epe1LQ3Dxk
"""

X, Y, A, B, C = map(int, input().split())


def _check(x, y, a, b):
    """面積a, bを[x, y]に配置できるか

    Args:
        x (int): 底にする辺
        y (int): 底にしない辺
        a (int): 底に接続させる四角形
        b (int): 底に接続させない四角形
    """
    base_y = -(-a // x)
    length_y = y - base_y
    return length_y * x >= b


def check(x, y, a, b, c):
    """面積a, b, c を [x, y]に配置できるか

    Args:
        x (int): 底にする辺
        y (int): 底ではない方の辺
        a (int): 底に接続させる四角形
        b (int): 底に接続させない四角形
        c (int): 底に接続させない四角形

    Returns:
        Bool: 配置できるかどうか
    """
    base_y = -(-a // x)
    length_y = y - base_y
    if length_y <= 0:
        return False
    return _check(x, length_y, b, c) | _check(length_y, x, b, c)


ans = (
    check(X, Y, A, B, C)
    | check(X, Y, B, A, C)
    | check(X, Y, C, A, B)
    | check(Y, X, A, B, C)
    | check(Y, X, B, A, C)
    | check(Y, X, C, A, B)
)

print("Yes" if ans else "No")
