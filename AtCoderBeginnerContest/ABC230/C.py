"""
C - X drawing
https://atcoder.jp/contests/abc230/tasks/abc230_c
"""

N, A, B = map(int, input().split())
P, Q, R, S = map(int, input().split())


def pattern1(i, j):
    Ak = i - A
    Bk = j - B

    if Ak != Bk:
        return False

    if max(1 - A, 1 - B) <= Ak <= min(N - A, N - B):
        return True
    else:
        return False


def pattern2(i, j):
    Ak = i - A
    Bk = B - j
    if Ak != Bk:
        return False

    if max(1 - A, B - N) <= Ak <= min(N - A, B - 1):
        return True
    else:
        return False


for i in range(P, Q + 1):
    grid = []
    for j in range(R, S + 1):
        if pattern1(i, j):
            grid.append("#")
        elif pattern2(i, j):
            grid.append("#")
        else:
            grid.append(".")

    print("".join(grid))
