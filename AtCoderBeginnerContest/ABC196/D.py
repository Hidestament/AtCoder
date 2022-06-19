"""
D - Hanjo
https://atcoder.jp/contests/abc196/tasks/abc196_d
"""
import sys

sys.setrecursionlimit(10**7)

H, W, A, B = map(int, input().split())


def dfs(i, bit, a, b):
    global ans
    if i == H * W:
        ans += 1
        return

    # 既にマスが置かれていたら次へ
    if bit & (1 << i):
        dfs(i + 1, bit, a, b)
        return

    # A横置き
    if (i % W != W - 1) and (not (bit & (1 << i + 1))) and a:
        dfs(i + 1, bit | 1 << i | 1 << (i + 1), a - 1, b)

    # A縦置き
    if (i + W < H * W) and (not (bit & (1 << i + W))) and a:
        dfs(i + 1, bit | 1 << i | 1 << (i + W), a - 1, b)

    # B起き
    if b:
        dfs(i + 1, bit | 1 << i, a, b - 1)


ans = 0
dfs(0, 0, A, B)
print(ans)
