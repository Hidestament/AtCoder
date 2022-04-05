"""
F - typewriter
問題リンク: https://atcoder.jp/contests/abc246/tasks/abc246_f
包除原理で頑張る
"""


N, L = map(int, input().split())
S = []
mod = 998244353

for i in range(N):
    s = input()
    bit_s = 0
    for char in s:
        bit_s |= (1 << (ord(char) - ord("a")))
    S.append(bit_s)


def popcount(x):
    '''xの立っているビット数をカウントする関数
    (xは64bit整数)'''

    # 2bitごとの組に分け、立っているビット数を2bitで表現する
    x = x - ((x >> 1) & 0x5555555555555555)

    # 4bit整数に 上位2bit + 下位2bit を計算した値を入れる
    x = (x & 0x3333333333333333) + ((x >> 2) & 0x3333333333333333)

    x = (x + (x >> 4)) & 0x0f0f0f0f0f0f0f0f  # 8bitごと
    x = x + (x >> 8)  # 16bitごと
    x = x + (x >> 16)  # 32bitごと
    x = x + (x >> 32)  # 64bitごと = 全部の合計
    return x & 0x0000007f


ans = 0
for bits in range(1, 1 << N):
    # 使える文字の種類数を計算する
    num_char = (1 << 26) - 1
    cnt = 0
    for i in range(N):
        if (bits & (1 << i)):
            num_char &= S[i]
            cnt += 1
    num_char = popcount(num_char)
    ans += (-1)**(popcount(bits)+1) * pow(num_char, L, mod)
    ans %= mod

print(ans)


mod = 10**9 + 7
N = 10**5

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
