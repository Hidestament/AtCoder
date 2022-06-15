"""
B - Visibility
https://atcoder.jp/contests/abc197/tasks/abc197_b
"""

H, W, X, Y = map(int, input().split())
grid = [input() for _ in range(H)]

X -= 1
Y -= 1

ans = 0

for dx in range(H):
    nx = X + dx
    if nx >= H:
        break
    if grid[nx][Y] == "#":
        break
    ans += 1

for dx in range(H):
    nx = X - dx
    if nx < 0:
        break
    if grid[nx][Y] == "#":
        break
    ans += 1

for dy in range(W):
    ny = Y + dy
    if ny >= W:
        break
    if grid[X][ny] == "#":
        break
    ans += 1

for dy in range(W):
    ny = Y - dy
    if ny < 0:
        break
    if grid[X][ny] == "#":
        break
    ans += 1

print(ans - 3)
