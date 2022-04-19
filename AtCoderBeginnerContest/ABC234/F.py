"""
F - Reordering
https://atcoder.jp/contests/abc234/tasks/abc234_f
"""


from collections import defaultdict


S = str(input())
mod = 998244353

N = 10**6
fact = [1] * (N+1)  # fact[i] = i! % mod
inv = [1] * (N+1)  # inv[i] = i^-1 % mod, factinvの計算用
inv[0] = 0
factinv = [1] * (N+1)  # factinv[i] = (i!)^-1 % mod

for i in range(2, N+1):
    fact[i] = (fact[i-1] * i) % mod
    inv[i] = (-inv[mod % i] * (mod // i)) % mod
    factinv[i] = (factinv[i-1] * inv[i]) % mod


def cmb_mod(n, r):
    if (r < 0) or (n < r):
        return 0
    r = min(r, n-r)
    return fact[n] * factinv[r] * factinv[n-r] % mod


# まずはどの文字が何文字使えるかのcnt
cnt = defaultdict(int)
for s in S:
    num = ord(s) - 96
    cnt[num] += 1

# DP[s][i]: s番目までの文字を使って, 長さiの文字列を作る数
DP = [[0] * (len(S) + 1) for _ in range(27)]
DP[0][0] = 1  # どれも使わない文字列は空文字列1つ

for s in range(26):
    num = cnt[s + 1]  # 使える文字数
    for i in range(len(S) + 1):  # これまでの文字数
        if DP[s][i] == 0:
            continue
        for j in range(num + 1):  # sから使う文字数
            if i + j <= len(S):
                DP[s + 1][i + j] += DP[s][i] * cmb_mod(i+j, j)
                DP[s + 1][i + j] %= mod

print((sum(DP[-1]) - 1) % mod)
