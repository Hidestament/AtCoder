"""
D - Flip Cards
https://atcoder.jp/contests/abc291/tasks/abc291_d
"""

MOD = 998244353

N = int(input())
cards = [list(map(int, input().split())) for _ in range(N)]


# DP[i][flip]: i番目まで決まっていて, 相違なるようにできる場合の数
#              flip=0: i番目をflipしない, flip=1: する
DP = [[0, 0] for _ in range(N + 1)]

# 0番目はダミー
DP[0][0] = 1

for i in range(N):
    a, b = cards[i]

    if i == 0:
        prev_a, prev_b = -1, -1
    else:
        prev_a, prev_b = cards[i - 1]

    # i-1番目をflipさせてなかった場合
    if DP[i][0]:
        # 表・表
        if prev_a != a:
            DP[i + 1][0] += DP[i][0]
            DP[i + 1][0] %= MOD
        # 表・裏
        if prev_a != b:
            DP[i + 1][1] += DP[i][0]
            DP[i + 1][1] %= MOD

    # i-1番目をflipさせてた場合
    if DP[i][1]:
        # 裏・表
        if prev_b != a:
            DP[i + 1][0] += DP[i][1]
            DP[i + 1][0] %= MOD
        # 裏・裏
        if prev_b != b:
            DP[i + 1][1] += DP[i][1]
            DP[i + 1][1] %= MOD


print(sum(DP[-1]) % MOD)
