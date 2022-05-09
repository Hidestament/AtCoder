"""
C - Adjacent Swaps
https://atcoder.jp/contests/abc250/tasks/abc250_c
"""
N, Q = map(int, input().split())
A = [i for i in range(1, N + 1)]

# ind[i]: 数字iのindex
ind = {i: i - 1 for i in range(1, N + 1)}

for _ in range(Q):
    x = int(input())
    if ind[x] == N - 1:  # 左とswap
        left = A[N - 2]
        ind[left] += 1
        ind[x] -= 1
        A[N - 2], A[N - 1] = A[N - 1], A[N - 2]
    else:  # 右とswap
        i = ind[x]
        right = A[i + 1]
        A[i], A[i + 1] = A[i + 1], A[i]
        ind[x] += 1
        ind[right] -= 1

print(*A)
