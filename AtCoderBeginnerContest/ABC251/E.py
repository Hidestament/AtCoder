"""
E - Takahashi and Animals
https://atcoder.jp/contests/abc251/tasks/abc251_e
"""
N = int(input())
A = list(map(int, input().split()))
INF = 10**15

# DP1[i][flag]: 辺iまで考えたときの最小値. flag=1なら辺iを選ぶ. 但し辺Nを選んでない
DP1 = [[INF] * 2 for _ in range(N)]
DP1[0][0] = 0

# DP2[i][flag]: Nを選んだ場合
DP2 = [[INF] * 2 for _ in range(N)]
DP2[0][1] = A[-1]

for i in range(1, N):
    a = A[i - 1]
    # i-1選ぶ -> i選ぶ
    DP1[i][1] = min(DP1[i][1], DP1[i - 1][1] + a)
    DP2[i][1] = min(DP2[i][1], DP2[i - 1][1] + a)

    # i-1選ばない -> i選ぶ
    DP1[i][1] = min(DP1[i][1], DP1[i - 1][0] + a)
    DP2[i][1] = min(DP2[i][1], DP2[i - 1][0] + a)

    # i-1選ぶ -> i選ばない
    DP1[i][0] = min(DP1[i][0], DP1[i - 1][1])
    DP2[i][0] = min(DP2[i][0], DP2[i - 1][1])

# DP1の場合, 絶対辺N-1を選ばないといけない
# DP2の場合, 辺N-1は選んでも選ばなくてもどちらでも良い
ans = min(DP1[-1][1], DP2[-1][0], DP2[-1][1])
print(ans)
