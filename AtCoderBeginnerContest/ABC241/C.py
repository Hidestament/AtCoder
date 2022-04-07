"""
C - Connect 6
https://atcoder.jp/contests/abc241/tasks/abc241_c
"""

N = int(input())
grid = [[0] * N for _ in range(N)]

for h in range(N):
    S = str(input())
    for w, s in enumerate(S):
        if s == "#":
            grid[h][w] = 1

flag = False
for h in range(N):
    for w in range(N):
        # (h, w)から右へ6マス
        if w + 5 < N:
            yoko = sum(grid[h][x] for x in range(w, w+6))
            if yoko >= 4:
                flag = True

        # (h, w)から下へ6マス
        if h + 5 < N:
            tate = sum(grid[x][w] for x in range(h, h+6))
            if tate >= 4:
                flag = True

        # (h, w)から右斜下へ6マス
        if (h + 5 < N) and (w + 5 < N):
            right_naname = sum(grid[h+k][w+k] for k in range(6))
            if right_naname >= 4:
                flag = True

        # (h, w)から左斜下へ6マス
        if (h + 5 < N) and (0 <= w - 5):
            left_naname = sum(grid[h+k][w-k] for k in range(6))
            if left_naname >= 4:
                flag = True

print("Yes" if flag else "No")
