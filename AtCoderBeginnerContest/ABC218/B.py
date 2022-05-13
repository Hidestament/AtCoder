"""
B - qwerty
https://atcoder.jp/contests/abc218/tasks/abc218_b
"""
P = list(map(int, input().split()))

S = ""
for p in P:
    S += chr(ord("a") + (p - 1))
print(S)
