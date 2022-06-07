"""
C - IPFL
https://atcoder.jp/contests/abc199/tasks/abc199_c
pythonのリストが参照渡しであることを利用
"""

N = int(input())
S = str(input())
Q = int(input())

S = [list(S[:N]), list(S[N:])]
for _ in range(Q):
    t, a, b = map(int, input().split())
    a -= 1
    b -= 1
    if t == 1:
        if (a < N) and (b < N):
            S[0][a], S[0][b] = S[0][b], S[0][a]
        elif (a < N) and (b >= N):
            S[0][a], S[1][b - N] = S[1][b - N], S[0][a]
        else:
            S[1][a - N], S[1][b - N] = S[1][b - N], S[1][a - N]
    else:
        S[0], S[1] = S[1], S[0]

print("".join(S[0]) + "".join(S[1]))
