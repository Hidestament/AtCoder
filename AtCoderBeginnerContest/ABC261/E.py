"""
E - Many Operations
https://atcoder.jp/contests/abc261/tasks/abc261_e
参考: https://mono-0812.hatenablog.com/entry/20220724/1658592959
"""

N, C = map(int, input().split())

C = bin(C)[2:].zfill(32)
C = list(map(int, C))

# now_operation[i][0 or 1]: iビット目が0 or 1 のときに, 何の値になるか
operations = [[0, 1] for _ in range(len(C))]

for _ in range(N):
    t, a = map(int, input().split())
    a = bin(a)[2:].zfill(32)
    a = list(map(int, a))

    # 操作の更新
    if t == 1:
        for k in range(len(C)):
            if a[k] == 0:
                operations[k] = [0, 0]
    elif t == 2:
        for k in range(len(C)):
            if a[k] == 1:
                operations[k] = [1, 1]
    else:
        for k in range(len(C)):
            if a[k] == 1:
                operations[k] = [
                    int(not operations[k][0]),
                    int(not operations[k][1]),
                ]

    # Cの更新
    for k, bit in enumerate(C):
        C[k] = operations[k][bit]

    print(int("".join(map(str, C)), 2))
