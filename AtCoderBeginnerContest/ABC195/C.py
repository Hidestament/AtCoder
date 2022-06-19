"""
C - Comma
https://atcoder.jp/contests/abc195/tasks/abc195_c
"""

N = int(input())

ans = 0
for dig in range(len(str(N))):
    if dig == len(str(N)) - 1:
        ans += (N - pow(10, dig) + 1) * (dig // 3)
    else:
        ans += (pow(10, dig + 1) - pow(10, dig)) * (dig // 3)

print(ans)
