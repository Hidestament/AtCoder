"""
C - Calendar Validator
https://atcoder.jp/contests/abc225/tasks/abc225_c
"""

N, M = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(N)]

flag = True
# 縦方向のcheck
for i in range(N - 1):
    if B[i + 1][0] - B[i][0] != 7:
        flag = False

# 横方向のcheck
for i in range(N):
    for j in range(M - 1):
        if B[i][j + 1] - B[i][j] != 1:
            flag = False
        if (B[i][j] % 7 == 0) and (M >= 2):
            flag = False

print("Yes" if flag else "No")
