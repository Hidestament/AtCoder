"""
D - Left Right Operation
https://atcoder.jp/contests/abc263/tasks/abc263_d
"""

N, L, R = map(int, input().split())
A = list(map(int, input().split()))

# DP1[i][flag]: 左からi番目までの総和の最小値.
# flag=0 -> Lに置き換える. flag=1 -> Lに置き換えない
DP1 = [[float("inf")] * 2 for _ in range(N + 1)]
DP1[0][0] = 0
DP1[0][1] = 0

for i in range(1, N + 1):
    # 置き換えない (flag=1) -> 置き換えない (flag=1)
    DP1[i][1] = min(DP1[i][1], DP1[i - 1][1] + A[i - 1])

    # 置き換える (flag=0) -> 置き換えない (flag=1)
    DP1[i][1] = min(DP1[i][1], DP1[i - 1][0] + A[i - 1])

    # 置き換える -> 置き換える
    DP1[i][0] = DP1[i - 1][0] + L


A = A[::-1]
# DP2[i][flag]: 右からi番目までの総和の最小値.
# flag=0 -> Lに置き換える. flag=1 -> Lに置き換えない
DP2 = [[float("inf")] * 2 for _ in range(N + 1)]
DP2[0][0] = 0
DP2[0][1] = 0

for i in range(1, N + 1):
    # 置き換えない (flag=1) -> 置き換えない (flag=1)
    DP2[i][1] = min(DP2[i][1], DP2[i - 1][1] + A[i - 1])

    # 置き換える (flag=0) -> 置き換えない (flag=1)
    DP2[i][1] = min(DP2[i][1], DP2[i - 1][0] + A[i - 1])

    # 置き換える -> 置き換える
    DP2[i][0] = DP2[i - 1][0] + R


ans = float("inf")
for i in range(N + 1):
    ans = min(ans, min(DP1[i]) + min(DP2[N - i]))

print(ans)
