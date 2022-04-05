"""
D - Polynomial division
問題リンク: https://atcoder.jp/contests/abc245/tasks/abc245_d
"""

N, M = map(int, input().split())
A = list(map(int, input().split()))
C = list(map(int, input().split()))

B = [None] * (M+1)
for ck in range(N+M+1):
    c = C[ck]
    flag = False
    for ak in range(N+1):
        bk = ck - ak
        if A[ak] == 0:
            continue
        if not (0 <= bk <= M):
            break

        if B[bk] is None:
            target_b = bk
            target_a = ak
            flag = True
        else:
            c -= A[ak] * B[bk]

    if flag:
        B[target_b] = c // A[target_a]


for k in range(M+1):
    if B[k] is None:
        B[k] = 0

print(*B)
