"""
C - Digital Graffiti
https://atcoder.jp/contests/abc191/tasks/abc191_c
"""

from itertools import product


H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]

for h, w in product(range(H), range(W)):
    if S[h][w] == "#":
        S[h][w] = 1
    else:
        S[h][w] = 0

ans = 0
for h, w in product(range(H - 1), range(W - 1)):
    s = S[h][w] + S[h + 1][w] + S[h][w + 1] + S[h + 1][w + 1]
    if (s == 1) or (s == 3):
        ans += 1

print(ans)
