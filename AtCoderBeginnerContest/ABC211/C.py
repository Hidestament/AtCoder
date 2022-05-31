"""
C - chokudai
https://atcoder.jp/contests/abc211/tasks/abc211_c
"""
S = str(input())
MOD = 10**9 + 7
table = {i: s for i, s in enumerate("chokudai", start=1)}
table[0] = "None"

# DP[i][x]: i文字目まででchokudaiのx文字目までを作る場合の数
DP = [[0] * 9 for _ in range(len(S) + 1)]
DP[0][0] = 1

for i in range(1, len(S) + 1):
    s = S[i - 1]
    for x in range(9):
        # S[i - 1]を使用する場合
        if table[x] == s:
            DP[i][x] += DP[i - 1][x - 1]
            DP[i][x] %= MOD

        # 使用しない場合
        DP[i][x] += DP[i - 1][x]
        DP[i][x] %= MOD

print(DP[-1][-1])
