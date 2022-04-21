"""
E - Minimal payments
https://atcoder.jp/contests/abc231/tasks/abc231_e
参考: https://note.com/syamashi/n/ncdace30186fa
"""


from bisect import bisect_left, bisect_right


N, X = map(int, input().split())
A = list(map(int, input().split()))
memo = {a: 1 for a in A}
memo[0] = 0


def dfs(x):
    """x円支払うのに必要な硬貨の枚数（おつり+支払い）

    Args:
        x: 対象金額

    Notes:
        x円支払うのに適切な硬貨は,
        x以上の最小の硬貨 or x以下の最大の硬貨のどちらかである.
    """
    # 既に計算してたら
    if x in memo:
        return memo[x]

    memo[x] = 1 << 64

    # x円以上の最大の硬貨
    if A[-1] >= x:
        upper_coin = A[bisect_left(A, x)]
        memo[x] = min(memo[x], 1 + dfs(upper_coin - x))

    # x円以下の最大の硬貨
    lower_coin = A[bisect_right(A, x) - 1]
    # ぴったり払う場合
    lower_coin_num = x // lower_coin
    res = x % lower_coin
    memo[x] = min(memo[x], lower_coin_num + dfs(res))
    # 余分に支払う場合
    if res:  # res=0 なら 余分に払うもクソもない
        lower_coin_num += 1
        change = x - lower_coin_num * lower_coin
        memo[x] = min(memo[x], lower_coin_num + dfs(change))

    return memo[x]


print(dfs(X))
