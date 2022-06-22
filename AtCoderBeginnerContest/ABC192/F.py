"""
F - Potion
https://atcoder.jp/contests/abc192/tasks/abc192_f
参考: https://note.com/momomo0214/n/n254aa1c75ade#PLB3a
"""
from itertools import product

N, X = map(int, input().split())
A = list(map(int, input().split()))
INF = 10**15


def solve(K):
    # DP[i][j][k]: i番目までの素材からj個選んで 和のmodがkになる最大の和
    DP = [[[-INF] * K for _ in range(K + 1)] for _ in range(N + 1)]
    DP[0][0][0] = 0

    for i, j, k in product(range(N), range(K + 1), range(K)):
        if DP[i][j][k] == -INF:
            continue

        a = A[i]

        # i番目の素材を選ぶとき
        if j + 1 <= K:
            DP[i + 1][j + 1][(k + a) % K] = max(
                DP[i + 1][j + 1][(k + a) % K], DP[i][j][k] + a
            )

        # i番目の素材を選ばないとき
        DP[i + 1][j][k] = max(DP[i + 1][j][k], DP[i][j][k])
    return DP[-1][K][X % K]


ans = 10**20
for k in range(1, N + 1):
    k_ans = solve(k)
    if k_ans != -INF:
        ans = min(ans, (X - k_ans) // k)

print(ans)
