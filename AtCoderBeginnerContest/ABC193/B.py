"""
B - Play Snuke
https://atcoder.jp/contests/abc193/tasks/abc193_b
"""

N = int(input())
INF = 10**15

ans = INF
for _ in range(N):
    a, p, x = map(int, input().split())
    res = max(0, x - a)
    if res:
        ans = min(ans, p)

print(ans if ans < INF else -1)
