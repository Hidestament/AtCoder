"""
C - Coupon
問題リンク: https://atcoder.jp/contests/abc246/tasks/abc246_c
2回探索する
"""


N, K, X = map(int, input().split())
A = list(map(int, input().split()))

A.sort(reverse=True)
cnt = 0
for i in range(N):
    # a >= kX, a/X >= k
    best_k = A[i] // X
    if best_k + cnt <= K:
        cnt += best_k
        A[i] -= X * best_k
    else:
        res = K - cnt
        A[i] -= X * res
        cnt = K
        break

if cnt < K:
    A.sort(reverse=True)
    for i in range(N):
        if cnt + 1 <= K:
            A[i] = 0
            cnt += 1
        else:
            break

print(sum(A))
