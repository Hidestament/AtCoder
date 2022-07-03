"""
D - Trophy
https://atcoder.jp/contests/abc258/tasks/abc258_d
"""

INF = float("INF")

N, X = map(int, input().split())
games = [list(map(int, input().split())) for _ in range(N)]

ans = INF
min_b = INF
all_sum = 0
for i in range(N):
    a, b = games[i]

    min_b = min(min_b, b)
    all_sum += a + b

    res = X - (i + 1)
    ans = min(ans, all_sum + min_b * res)

print(ans)
