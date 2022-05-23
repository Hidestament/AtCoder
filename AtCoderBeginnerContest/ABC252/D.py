"""
D - Distinct Trio
https://atcoder.jp/contests/abc252/tasks/abc252_d
"""
N = int(input())
A = list(map(int, input().split()))


def inclusive_solve():
    """異なる3組の選び方
    = 全ての選び方 - (同じ数字が2個) - (同じ数字が3個)
    """
    from collections import Counter

    counter = Counter(A)
    ans = N * (N - 1) * (N - 2) // 6  # NC3
    for _, cnt in counter.items():
        # 同じ数字2つの選び方 * その他の数字
        ans -= (cnt * (cnt - 1) // 2) * (N - cnt)
        # 同じ数字3つの選び方
        ans -= cnt * (cnt - 1) * (cnt - 2) // 6

    print(ans)


def center_bruteforce_solve():
    """真ん中の数字を全探索"""
    from collections import Counter
    from itertools import groupby

    A.sort()
    under_cnt = {}  # under_cnt[a]: a未満の数字の個数
    counter = Counter(A)
    total = 0
    for num, cnt in groupby(A):
        under_cnt[num] = total
        total += len(list(cnt))

    ans = 0
    for a in A:
        ans += under_cnt[a] * (N - counter[a] - under_cnt[a])
    print(ans)


# inclusive_solve()
center_bruteforce_solve()
