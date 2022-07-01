"""
B - Magic 3
https://atcoder.jp/contests/abc190/tasks/abc190_b
"""

N, S, D = map(int, input().split())
total_damage = 0
for _ in range(N):
    x, y = map(int, input().split())
    if (x >= S) or (y <= D):
        continue
    total_damage += y

print("Yes" if total_damage > 0 else "No")
