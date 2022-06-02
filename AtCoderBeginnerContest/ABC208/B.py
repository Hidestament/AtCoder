"""
B - Factorial Yen Coin
https://atcoder.jp/contests/abc208/tasks/abc208_b
"""
from math import factorial

P = int(input())
coins = [factorial(i) for i in range(10, 0, -1)]

ans = 0
for value in coins:
    ans += P // value
    P %= value
print(ans)
