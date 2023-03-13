"""
C - Make Takahashi Happy
https://atcoder.jp/contests/abc293/tasks/abc293_c
"""
import sys

sys.setrecursionlimit(10**6)

H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]

ans = 0


def dfs(h, w, seen):
    global ans
    if (h == H - 1) and (w == W - 1):
        ans += 1
        return

    # 右に移動
    if w < W - 1:
        a = A[h][w + 1]
        if a not in seen:
            seen.add(a)
            dfs(h, w + 1, seen)
            seen.discard(a)

    # 下に移動
    if h < H - 1:
        a = A[h + 1][w]
        if a not in seen:
            seen.add(a)
            dfs(h + 1, w, seen)
            seen.discard(a)


dfs(0, 0, set([A[0][0]]))
print(ans)
