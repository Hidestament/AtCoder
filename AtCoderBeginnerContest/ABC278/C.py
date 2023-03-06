"""
C - FF
https://atcoder.jp/contests/abc278/tasks/abc278_c
"""

N, Q = map(int, input().split())

follow = set()
for _ in range(Q):
    t, a, b = map(int, input().split())

    if t == 1:
        follow.add((a, b))
    elif t == 2:
        follow.discard((a, b))
    else:
        if ((a, b) in follow) and ((b, a) in follow):
            print("Yes")
        else:
            print("No")
