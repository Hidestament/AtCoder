"""
B - Broken Rounding
https://atcoder.jp/contests/abc273/tasks/abc273_b
"""
import sys

input = sys.stdin.readline

X, K = map(int, input().split())
for i in range(K):
    # Xのi桁目の数
    digit_i = (X // pow(10, i)) % 10
    res = X % pow(10, i + 1)

    # 切り捨て
    if 0 <= digit_i <= 4:
        X -= res
    # 切り上げ
    else:
        X += pow(10, i + 1) - res

print(X)
