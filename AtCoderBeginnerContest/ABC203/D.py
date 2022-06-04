"""
D - Pond
https://atcoder.jp/contests/abc203/tasks/abc203_d
参考: https://blog.hamayanhamayan.com/entry/2021/05/30/225914
    : https://qiita.com/drken/items/56a6b68edef8fc605821#4-%E4%BA%8C%E6%AC%A1%E5%85%83%E7%B4%AF%E7%A9%8D%E5%92%8C
"""
from itertools import product

N, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]


def calc_2d_sum(S, h1, w1, h2, w2):
    # (h1, w1) ~ (h2, w2)の累積和を計算する
    if (h1 == 0) and (w1 == 0):
        return S[h2][w2]
    if h1 == 0:
        return S[h2][w2] - S[h2][w1 - 1]
    if w1 == 0:
        return S[h2][w2] - S[h1 - 1][w2]
    return S[h2][w2] - S[h1 - 1][w2] - S[h2][w1 - 1] + S[h1 - 1][w1 - 1]


def check(x):
    """全ての区間の中央値がx以上か判定する
    => x以上のモノの個数が, (K^2/2 + 1)個あれば良い
    """
    # 全ての区間の中央値がx以上かを判定する
    S = [[int(A[h][w] >= x) for w in range(N)] for h in range(N)]
    # Sの2d累積和行列を計算
    for h in range(1, N):
        for w in range(N):
            S[h][w] += S[h - 1][w]
    for h in range(N):
        for w in range(1, N):
            S[h][w] += S[h][w - 1]

    # 全ての(K, K)区間について判定
    for h, w in product(range(N), range(N)):
        if (h + (K - 1) >= N) or (w + (K - 1) >= N):
            continue
        s = calc_2d_sum(S, h, w, h + (K - 1), w + (K - 1))
        if s < (K**2 // 2 + 1):
            return False
    return True


# 全ての(K, K)区間の中央値がx以上かどうか
left, right = 0, 10**10
while (right - left) > 1:
    mid = (left + right) // 2
    if check(mid):
        left = mid
    else:
        right = mid

print(left)
