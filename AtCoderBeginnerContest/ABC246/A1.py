"""
A - Four Points
問題リンク: https://atcoder.jp/contests/abc246/tasks/abc246_a
Xor で 解く
"""


points = [list(map(int, input().split())) for _ in range(3)]
x = points[0][0] ^ points[1][0] ^ points[2][0]
y = points[0][1] ^ points[1][1] ^ points[2][1]

print(x, y)
