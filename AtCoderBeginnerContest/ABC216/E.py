"""
E - Amusement Park
https://atcoder.jp/contests/abc216/tasks/abc216_e
参考: https://atcoder.jp/contests/abc216/editorial/2469
"""


def solve_tousa_sum():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A = sorted(A, reverse=True) + [0]

    def tousa_sum(a, b):
        n = a - b + 1
        return n * (a + b) // 2

    # 高さを揃える
    score = 0
    for i in range(N):
        diff = A[i] - A[i + 1]
        if K - (i + 1) * diff < 0:
            cycle = K // (i + 1)  # 何周できるか
            amari = K % (i + 1)  # 残り
            score += (i + 1) * tousa_sum(A[i], A[i] - cycle + 1)
            score += amari * (A[i] - cycle)
            break

        K -= (i + 1) * diff
        score += (i + 1) * tousa_sum(A[i], A[i + 1] + 1)
        A[i] -= diff

    print(score)


def solve_binary_search():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    # 数列Bの要素に含まれるx以上のモノの個数はK個以下か
    # 1. TrueとFalseの境目 -> x以上のモノの個数がちょうどK個ある
    # 2. x以上のアトラクションをK回乗れば良い
    def check(x):
        cnt = sum(max(0, a - x + 1) for a in A)
        return cnt <= K

    def tousa_sum(a, n):
        return n * (2 * a - (n - 1)) // 2

    # left: False, right: True:
    left, right = 0, 10**18
    while (right - left) > 1:
        mid = (left + right) // 2
        if check(mid):
            right = mid
        else:
            left = mid

    if check(left):
        ans = sum(tousa_sum(a, a - left + 1) for a in A)
    else:
        ans = sum(tousa_sum(a, max(0, a - right + 1)) for a in A)
        K -= sum(max(0, a - right + 1) for a in A)
        ans += (right - 1) * K
    print(ans)


# solve_tousa_sum()
solve_binary_search()
