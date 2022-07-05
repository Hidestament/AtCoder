"""
D - Choose Me
https://atcoder.jp/contests/abc187/tasks/abc187_d
"""

N = int(input())
ab = [list(map(int, input().split())) for _ in range(N)]

ab.sort(key=lambda x: 2 * x[0] + x[1], reverse=True)

aoki = sum(ab[i][0] for i in range(N))
takahashi = 0

ans = 0
for a, b in ab:
    takahashi += a + b
    aoki -= a
    ans += 1
    if takahashi > aoki:
        break

print(ans)
