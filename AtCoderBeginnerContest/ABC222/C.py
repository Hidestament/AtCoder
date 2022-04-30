"""
C - Swiss-System Tournament
https://atcoder.jp/contests/abc222/tasks/abc222_c
"""

N, M = map(int, input().split())
A = [str(input()) for _ in range(2 * N)]


def zyanken(a, b):
    if a == b:
        return "Draw"
    elif (a == "G") and (b == "C"):
        return a
    elif (a == "G") and (b == "P"):
        return b
    elif (a == "C") and (b == "G"):
        return b
    elif (a == "C") and (b == "P"):
        return a
    elif (a == "P") and (b == "G"):
        return a
    elif (a == "P") and (b == "C"):
        return b


# order[k]: [勝数, 番号]
order = [[0, i] for i in range(2 * N)]
for i in range(M):
    for k in range(1, 2 * N, 2):
        a = order[k][1]
        b = order[k - 1][1]
        results = zyanken(A[a][i], A[b][i])
        if results == "Draw":
            continue
        elif results == A[a][i]:
            order[k][0] += 1
        else:
            order[k - 1][0] += 1

    order.sort(key=lambda x: (-x[0], x[1]))

for i in range(2 * N):
    print(order[i][1] + 1)
