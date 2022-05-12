"""
E - Distance on Large Perfect Binary Tree
https://atcoder.jp/contests/abc220/tasks/abc220_e
参考: https://atcoder.jp/contests/abc220/editorial/2679
"""
N, D = map(int, input().split())
MOD = 998244353

ans = 0
for d in range(N):
    # 1. v = i or v = j の場合
    if d + D < N:
        ans += 2 * pow(2, d, MOD) * pow(2, D, MOD)
        ans %= MOD

    # 2. vの左部分木の深さk, 右部分木の深さ D - kから1つずつ選ぶ場合
    ans += (
        2
        * pow(2, d, MOD)
        * min(max(0, 2 * N - 2 * d - D - 1), D - 1)
        * pow(2, max(0, D - 2), MOD)
    )
    ans %= MOD

print(ans)
