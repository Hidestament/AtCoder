"""
E - Max Min
https://atcoder.jp/contests/abc247/tasks/abc247_e
区間の分割 + 尺取法
"""

from collections import deque


N, X, Y = map(int, input().split())
A = list(map(int, input().split()))


def split(A):
    """区間の分割を行う
    """
    split_A, now = [], []
    for a in A:
        if Y <= a <= X:
            now.append(a)
        else:
            if now:
                split_A.append(now)
                now = []

    if now:
        split_A.append(now)
    return split_A


def calc_section(A):
    """区間に対して, 条件を満たす[L, R]の個数を計算する
    """
    dq = deque()
    cnt = 0
    min_num, max_num = None, None
    min_cnt, max_cnt = 0, 0
    for i, a in enumerate(A):
        dq.append(a)
        if a == Y:
            min_cnt += 1
            min_num = a
        if a == X:
            max_cnt += 1
            max_num = a

        if (max_num == X) and (min_num == Y):
            # 現在のi ~ len(A) まで R は動いても条件を満たす
            cnt += len(A) - i
            while dq:
                rm = dq.popleft()
                if rm == X:
                    max_cnt -= 1
                if rm == Y:
                    min_cnt -= 1

                if max_cnt == 0:
                    max_num = None
                    break
                if min_cnt == 0:
                    min_num = None
                    break

                if (max_num == X) and (min_num == Y):
                    cnt += len(A) - i
    return cnt


A = split(A)
ans = sum(calc_section(a) for a in A)
print(ans)
