"""
E - (∀x∀)
問題リンク: https://atcoder.jp/contests/abc242/tasks/abc242_e
桁DPのようなものを行う.
回文の文字列を作るには, 基本的に貪欲に前から半分まで決めれば良い
"""

T = int(input())
mod = 998244353

for _ in range(T):
    N = int(input())
    S = str(input())
    # 回文なので, 半分まで決定すれば十分
    half = -(-N//2)

    # DP[i][smaller]: i桁目を考えたときに, S以下となる回文Xの個数
    # smaller = Trueなら小さいことが確定, Falseなら未確定
    DP = [[0, 0] for _ in range(half + 1)]
    DP[0][0] = 1

    for i in range(1, half + 1):
        s = ord(S[i-1]) - ord("A") + 1
        # 未確定 -> 未確定
        DP[i][0] += DP[i-1][0]
        DP[i][0] %= mod

        # 未確定 -> 確定
        DP[i][1] += (s-1) * DP[i-1][0]
        DP[i][1] %= mod

        # 確定 -> 確定
        DP[i][1] += 26 * DP[i-1][1]
        DP[i][1] %= mod

    # 最後まで未確定だったものは, それが回文とは限らない
    ans = sum(DP[-1])
    if N % 2 == 0:
        if (S[:N//2] + S[:N//2][::-1]) > S:
            ans -= 1
    else:
        if (S[:N//2] + S[N//2] + S[:N//2][::-1]) > S:
            ans -= 1

    print(ans % mod)
