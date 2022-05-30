"""
B - Distance Between Tokens
https://atcoder.jp/contests/abc253/tasks/abc253_b
"""
from itertools import product

H, W = map(int, input().split())
grid = [input() for _ in range(H)]

mas = []
for h, w in product(range(H), range(W)):
    if grid[h][w] == "o":
        mas.append([h, w])

h1, w1 = mas[0]
h2, w2 = mas[1]
print(abs(h1 - h2) + abs(w1 - w2))
