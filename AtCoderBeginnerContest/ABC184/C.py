"""
C - Super Ryuma
https://atcoder.jp/contests/abc184/tasks/abc184_c
"""

r1, c1 = map(int, input().split())
r2, c2 = map(int, input().split())


def judge_one_move(a, b, c, d):
    """(a, b) -> (c, d)に一手で移動できるか

    Returns:
        bool: 一手で移動可能かどうかのbool値
    """
    if a + b == c + d:
        return True
    if a - b == c - d:
        return True
    if abs(a - c) + abs(b - d) <= 3:
        return True
    return False


if (r1, c1) == (r2, c2):
    print(0)
    exit()

if judge_one_move(r1, c1, r2, c2):
    print(1)
    exit()

# 2手でいける箇所
for dr in range(-4, 4):
    for dc in range(-4, 4):
        nr, nc = r1 + dr, c1 + dc
        if judge_one_move(r1, c1, nr, nc) and judge_one_move(nr, nc, r2, c2):
            print(2)
            exit()

# 市松模様の箇所
if (r1 + c1) % 2 == (r2 + c2) % 2:
    print(2)
    exit()

print(3)
