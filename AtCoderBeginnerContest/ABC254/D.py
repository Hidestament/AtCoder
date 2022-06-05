"""
D - Together Square
https://atcoder.jp/contests/abc254/tasks/abc254_d
参考: https://atcoder.jp/contests/abc254/editorial/4069
"""

N = int(input())

ans = 0
for i in range(1, N + 1):
    base = i
    # iを平方数で割れるだけ割る O(√N)
    d = 2
    while d**2 <= base:
        if base % (d**2) == 0:
            base //= d**2
        else:
            d += 1

    # baseに平方数をかけられるだけ掛ける O(√N)
    d = 1
    while (d**2) * base <= N:
        ans += 1
        d += 1

print(ans)
