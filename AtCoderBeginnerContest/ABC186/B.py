"""
B - Blocks on Grid
https://atcoder.jp/contests/abc186/tasks/abc186_b
"""

H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]

min_A = 10**10
for h in range(H):
    min_A = min(min_A, min(A[h]))

ans = 0
for h in range(H):
    for w in range(W):
        ans += A[h][w] - min_A

print(ans)
