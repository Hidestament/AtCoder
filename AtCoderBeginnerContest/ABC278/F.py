"""
F - Shiritori
https://atcoder.jp/contests/abc278/tasks/abc278_f
"""


def popcount(x):
    """xの立っているビット数をカウントする関数
    (xは64bit整数)"""

    # 2bitごとの組に分け、立っているビット数を2bitで表現する
    x = x - ((x >> 1) & 0x5555555555555555)

    # 4bit整数に 上位2bit + 下位2bit を計算した値を入れる
    x = (x & 0x3333333333333333) + ((x >> 2) & 0x3333333333333333)

    x = (x + (x >> 4)) & 0x0F0F0F0F0F0F0F0F  # 8bitごと
    x = x + (x >> 8)  # 16bitごと
    x = x + (x >> 16)  # 32bitごと
    x = x + (x >> 32)  # 64bitごと = 全部の合計
    return x & 0x0000007F


N = int(input())
S = [str(input()) for _ in range(N)]


# DP[s][v]: 訪問した文字の集合がsで, 最後に訪れた単語がvのときの勝者
DP = [[-1] * N for _ in range(1 << N)]

for s in range(1 << N)[::-1]:
    turn = popcount(s) % 2

    for now in range(N):
        if (s != 0) and (s & (1 << now)) == 0:
            continue

        # 次に行ける先
        can_move = []
        for to in range(N):
            if (s != 0) and (s & (1 << to)) == 1:
                continue
            if (s != 0) and (S[now][-1] != S[to][0]):
                continue

            can_move.append(to)

        # 次の行き先がどこにもない場合, 現在のターンの人が負け
        if not can_move:
            winner = 1 - turn
            DP[s][now] = winner
        else:
            winners = [DP[s | 1 << to][to] for to in can_move]
            if turn in winners:
                DP[s][now] = turn
            else:
                DP[s][now] = 1 - turn

print("First" if DP[0][0] == 0 else "Second")
