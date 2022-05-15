"""
E - Chain Contestant
https://atcoder.jp/contests/abc215/tasks/abc215_e
"""

N = int(input())
S = str(input())
MOD = 998244353

table = {chr(ord("A") + i): i for i in range(10)}

# DP[i][s][last]: i番目のコンテストまで考えたときに,
# これまで参加したコンテストの集合がs, 最後に参加したコンテストがlastの場合の数
DP = [[[0] * 11 for _ in range(1 << 10)] for _ in range(N + 1)]
DP[0][0][0] = 1

for i in range(1, N + 1):
    c = table[S[i - 1]]
    for s in range(1 << 10):
        # 初めてcに参加する場合
        if not (s & (1 << c)):
            for last in range(11):
                DP[i][s | 1 << c][c] += DP[i - 1][s][last]
                DP[i][s | 1 << c][c] %= MOD

        # 既に参加した場合
        if s & (1 << c):
            DP[i][s][c] += DP[i - 1][s][c]
            DP[i][s][c] %= MOD

        # 参加しない場合
        for last in range(11):
            DP[i][s][last] += DP[i - 1][s][last]
            DP[i][s][last] %= MOD

ans = sum(sum(DP[N][i]) for i in range(1, 1 << 10))
print(ans % MOD)
