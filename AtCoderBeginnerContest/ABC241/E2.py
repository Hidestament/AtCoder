"""
E - Putting Candies
https://atcoder.jp/contests/abc241/tasks/abc241_e
ダブリングで解く
"""

N, K = map(int, input().split())
A = list(map(int, input().split()))

# double[k][i]: iの2^k先の場所
double = [[(i+x) % N for i, x in enumerate(A)]]
# s_double[k][i]: iの2^k先の和
s_double = [A[:]]

s = pow(2, 1)
while s <= K:
    # double[k+1][i] = double[k][doubke[k][i]]
    next_double = [0] * N
    prev = double[-1]

    next_s = [0] * N
    prev_s = s_double[-1]

    for i in range(N):
        next_double[i] = prev[prev[i]]
        # 和 = 前の状態の和 + 次の状態の和
        next_s[i] = prev_s[prev[i]] + prev_s[i]

    double.append(next_double)
    s_double.append(next_s)

    s *= 2

X, pos = 0, 0
for i in range(len(double)):
    if K & (1 << i):
        X += s_double[i][pos]
        pos = double[i][pos]

print(X)
