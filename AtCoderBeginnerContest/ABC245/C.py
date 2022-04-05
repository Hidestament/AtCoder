"""
C - Choose Elements
問題リンク: https://atcoder.jp/contests/abc245/tasks/abc245_c
"""

N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# DP[i][flag]: i番目まで考えたときに, Xが存在するか
# flag = 0 なら, X[i] = A[i], flag =1 ならX[i] = B[i] とする
DP = [[False, False] for _ in range(N)]
DP[0][0], DP[0][1] = True, True

for i in range(1, N):
    # A[i-1] -> A[i]
    if DP[i-1][0] and abs(A[i-1] - A[i]) <= K:
        DP[i][0] = True

    # B[i-1] -> A[i]
    if DP[i-1][1] and abs(B[i-1] - A[i]) <= K:
        DP[i][0] = True

    # A[i-1] -> B[i]
    if DP[i-1][0] and abs(A[i-1] - B[i]) <= K:
        DP[i][1] = True

    # B[i-1] -> B[i]
    if DP[i-1][1] and abs(B[i-1] - B[i]) <= K:
        DP[i][1] = True

print("Yes" if DP[-1][0] or DP[-1][1] else "No")
