"""
E - Sequence Matching
https://atcoder.jp/contests/abc185/tasks/abc185_e
参考: https://drken1215.hatenablog.com/entry/2020/12/14/000300
"""

INF = 10**19

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# DP[i][j]: A[:i] と B[:j]の最適値
DP = [[INF] * (M + 1) for _ in range(N + 1)]

# 初期値
for i in range(N + 1):
    DP[i][0] = i

for j in range(M + 1):
    DP[0][j] = j

for i in range(1, N + 1):
    for j in range(1, M + 1):
        # A[i]を消して, B[j - 1]とマッチさせる
        DP[i][j] = min(DP[i][j], DP[i - 1][j] + 1)

        # B[j]を消して, A[i - 1]とマッチさせる
        DP[i][j] = min(DP[i][j], DP[i][j - 1] + 1)

        # A[i], B[j]の末尾を採用する
        if A[i - 1] == B[j - 1]:
            # 一致してるならコストはかからない
            DP[i][j] = min(DP[i][j], DP[i - 1][j - 1])
        else:
            DP[i][j] = min(DP[i][j], DP[i - 1][j - 1] + 1)

print(DP[-1][-1])
