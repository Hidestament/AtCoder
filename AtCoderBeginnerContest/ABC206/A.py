"""
A - Maxi-Buying
https://atcoder.jp/contests/abc206/tasks/abc206_a
"""
N = int(input())
price = (108 * N) // 100

if price < 206:
    print("Yay!")
elif price == 206:
    print("so-so")
else:
    print(":(")
