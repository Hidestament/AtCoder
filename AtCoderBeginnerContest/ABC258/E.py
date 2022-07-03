"""
E - Packing Potatoes
https://atcoder.jp/contests/abc258/tasks/abc258_e
参考: https://qiita.com/Kept1994/items/ea91c057b0e552323da3
"""

from math import log2


N, Q, X = map(int, input().split())
W = list(map(int, input().split()))

# C[i]: W[i]からstartした場合に, 箱に入れるじゃがいもの個数
sum_W = sum(W)
C = [N * (X // sum_W)] * N

# 尺取法でCを計算
all_sum = sum_W * (X // sum_W)
num_w = 0
right = 0
for left in range(N):
    while all_sum < X:
        all_sum += W[right]
        right = (right + 1) % N
        num_w += 1

    C[left] += num_w
    num_w -= 1
    all_sum -= W[left]


# ダブリング
max_log_K = int(log2(10**12 + 10)) + 5

# dv[k][i]: iから2^k回操作を行ったあとのstart地点
dv = [[-1] * N for _ in range(max_log_K)]

# dv[0][i] つまり iの次のstart地点をまずは求める
for i in range(N):
    dv[0][i] = (i + C[i]) % N

# 一般のkについて求める
for k in range(1, max_log_K):
    for i in range(N):
        dv[k][i] = dv[k - 1][dv[k - 1][i]]


for _ in range(Q):
    k = int(input()) - 1

    now = 0
    for dig in range(max_log_K + 1):
        if k & (1 << dig):
            now = dv[dig][now]
    print(C[now])
