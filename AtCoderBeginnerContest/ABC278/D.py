"""
D - All Assign Point Add
https://atcoder.jp/contests/abc278/tasks/abc278_d
"""

N = int(input())
A = list(map(int, input().split()))
Q = int(input())

base = -1
updated = set()
for _ in range(Q):
    query = list(map(int, input().split()))

    if query[0] == 1:
        x = query[1]
        base = x
        updated = set()

    elif query[0] == 2:
        i, x = query[1], query[2]
        i -= 1

        if base == -1:
            A[i] += x
        else:
            if i in updated:
                A[i] += x
            else:
                A[i] = base + x
                updated.add(i)

    else:
        i = query[1]
        i -= 1

        if (base != -1) and (i not in updated):
            A[i] = base
            updated.add(i)

        print(A[i])
