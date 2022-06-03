"""
E - Divide Both
https://atcoder.jp/contests/abc206/tasks/abc206_e
"""

L, R = map(int, input().split())

# cnt[g]: gcd(x,y) = gとなるような数字の組合せ
cnt = [0] * (R + 1)
for g in range(R, 1, -1):
    cnt[g] = (R // g - (L - 1) // g) ** 2
    gd = 2 * g
    while gd <= R:
        cnt[g] -= cnt[gd]
        gd += g

ans = 0
for g in range(2, R + 1):
    ans += cnt[g]
    if L <= g <= R:
        ans -= 2 * (R // g - (L - 1) // g) - 1

print(ans)
