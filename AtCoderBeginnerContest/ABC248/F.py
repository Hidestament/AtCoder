"""
F - Keep Connect
https://atcoder.jp/contests/abc248/tasks/abc248_f
連結DP
"""

N, P = map(int, input().split())

# DP1[i][k]: 上限が連結で, i列目まで決定していて, 削除した辺の個数がkであるような削除の仕方の個数
# DP2[i][k]: 上限が非連結で, i列目まで決定していて, 削除した辺の個数がkであるような削除の仕方の個数
DP1 = [[0 for _ in range(N+10)] for _ in range(N+1)]
DP2 = [[0 for _ in range(N+10)] for _ in range(N+1)]

DP1[1][0] = 1
DP2[1][1] = 1

for i in range(1, N):
    for k in range(N + 8):
        # 上の辺だけ残す -> 上下連結は変化しない(元々非連結だと駄目)
        DP2[i + 1][k + 2] += 2 * DP1[i][k]
        DP2[i + 1][k + 2] %= P

        # 上・中だけ残す -> 上下連結になる
        DP1[i + 1][k + 1] += 2 * DP1[i][k]
        DP1[i + 1][k + 1] %= P

        # 上・下だけ残す -> 連結度は変わらない
        DP1[i + 1][k + 1] += DP1[i][k]
        DP2[i + 1][k + 1] += DP2[i][k]
        DP1[i + 1][k + 1] %= P
        DP2[i + 1][k + 1] %= P

        # 全部残す -> 問答無用で連結
        DP1[i + 1][k] += DP2[i][k] + DP1[i][k]
        DP1[i + 1][k] %= P

for i in range(1, N):
    print(DP1[N][i])
