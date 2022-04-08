"""
D - AND and SUM
https://atcoder.jp/contests/abc238/tasks/abc238_d
この解法: https://qiita.com/u2dayo/items/12ac3e1834ededba1824#d%E5%95%8F%E9%A1%8Cand-and-sum
"""

T = int(input())
for _ in range(T):
    a, s = map(int, input().split())
    ds = s - 2*a

    if (ds >= 0) and ((ds & a) == 0):
        print("Yes")
    else:
        print("No")
