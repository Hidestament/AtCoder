"""
D - Base n
https://atcoder.jp/contests/abc192/tasks/abc192_d
"""

X = str(input())
M = int(input())
d = int(max(X))


def to_base_n(n):
    s = 0
    for i, x in enumerate(X[::-1]):
        s += int(x) * pow(n, i)
    return s


def check(n):
    x = to_base_n(n)
    return x <= M


if len(X) == 1:
    print(1 if check(d + 1) else 0)
    exit()


left, right = 0, 10**19
while (right - left) > 1:
    mid = (left + right) // 2
    if check(mid):
        left = mid
    else:
        right = mid

print(max(0, left - d))
