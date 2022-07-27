"""
D - increment of coins
https://atcoder.jp/contests/abc184/tasks/abc184_d
"""

A, B, C = map(int, input().split())

# DP[a][b][c]: coinが(a, b, c)であるときの期待値
DP = [[[0] * 101 for _ in range(101)] for _ in range(101)]

# 初期状態: DP[a][b][c]の a = 100 or b = 100 or c = 100なら操作の期待値は0
for a in range(100)[::-1]:
    for b in range(100)[::-1]:
        for c in range(100)[::-1]:
            DP[a][b][c] += (a / (a + b + c)) * (1 + DP[a + 1][b][c])
            DP[a][b][c] += (b / (a + b + c)) * (1 + DP[a][b + 1][c])
            DP[a][b][c] += (c / (a + b + c)) * (1 + DP[a][b][c + 1])

            if c == C:
                break
        if b == B:
            break
    if a == A:
        break


print(DP[A][B][C])
