"""
A - Adjacent Squares
https://atcoder.jp/contests/abc250/tasks/abc250_a
"""
H, W = map(int, input().split())
R, C = map(int, input().split())

ans = 0
for dh, dw in zip([1, 0, -1, 0], [0, 1, 0, -1]):
    nr, nc = R + dh, C + dw
    if 1 <= nr <= H and 1 <= nc <= W:
        ans += 1

print(ans)
