"""
C - Not Equal
https://atcoder.jp/contests/abc209/tasks/abc209_c
"""
N = int(input())
C = sorted(list(map(int, input().split())))
MOD = 10**9 + 7

ans = 1
for i, c in enumerate(C):
    ans *= c - i
    ans %= MOD
print(ans)
