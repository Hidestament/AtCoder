"""
C - Filling 3x3 array
https://atcoder.jp/contests/abc256/tasks/abc256_c
"""
import sys

sys.setrecursionlimit(10**7)


h1, h2, h3, w1, w2, w3 = map(int, input().split())
H = [h1, h2, h3]
W = [w1, w2, w3]


A = [[-1] * 3 for _ in range(3)]
ans = 0


def check(a):
    for h in range(3):
        if not sum(a[h][w] for w in range(3)) == H[h]:
            return False
    for w in range(3):
        if not sum(a[h][w] for h in range(3)) == W[w]:
            return False
    return True


def dfs(h, w, a):
    global ans
    if w == 3:
        w = 0
        h += 1
    if h == 3:
        if check(a):
            ans += 1
        return

    if w == 2:
        a_value = H[h] - a[h][0] - a[h][1]
        if a_value <= 0:
            return
        a[h][w] = a_value
        dfs(h, w + 1, a)
    elif h == 2:
        a_value = W[w] - a[0][w] - a[1][w]
        if a_value <= 0:
            return
        a[h][w] = a_value
        dfs(h, w + 1, a)
    else:
        for a_value in range(1, 31):
            a[h][w] = a_value
            dfs(h, w + 1, a)


dfs(0, 0, A)
print(ans)
