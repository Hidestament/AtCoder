"""
B - Go Straight and Turn Right
問題リンク: https://atcoder.jp/contests/abc244/tasks/abc244_b
複素数使って解く
"""

N = int(input())
T = str(input())

now = 0 + 0j
direction = 1 + 0j

for t in T:
    if t == "S":
        now += direction
    else:
        direction *= -1j

print(int(now.real), int(now.imag))
