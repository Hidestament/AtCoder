"""
B - Misjudge the Time
https://atcoder.jp/contests/abc278/tasks/abc278_b
"""

H, M = map(int, input().split())


def misjudged(h, m):
    rh = h - (h % 10) + (m // 10)
    rm = 10 * (h % 10) + (m % 10)

    if (0 <= rh <= 23) and (0 <= rm <= 59):
        return True
    else:
        return False


while True:
    if misjudged(H, M):
        print(H, M)
        exit()

    if M == 59:
        M = 0
        H = (H + 1) % 24
    else:
        M += 1
