"""
D - Online games
https://atcoder.jp/contests/abc221/tasks/abc221_d
"""
from itertools import accumulate


def compress(A):
    B = sorted(set(A))
    zipped = {}
    unzipped = {}
    for i, x in enumerate(B):
        zipped[x] = i
        unzipped[i] = x
    return zipped, unzipped


def solve_compress_and_imos():
    """imos法 + 座標圧縮"""
    N = int(input())
    used = [0, 10**100 + 1]
    cnt = [0] * (N + 1)
    event = []
    for _ in range(N):
        a, b = map(int, input().split())
        used.append(a)
        used.append(a + b)
        event.append([a, a + b])

    zipped, unzipped = compress(used)
    imos = [0] * len(zipped)
    for a, b in event:
        a, b = zipped[a], zipped[b]
        imos[a] += 1
        imos[b] -= 1
    imos = list(accumulate(imos))

    for i, num in enumerate(imos[:-1]):
        days = unzipped[i + 1] - unzipped[i]
        cnt[num] += days

    print(*cnt[1:])


def solve_event_sort():
    """ログインを+1, ログアウトを-1という別々のイベントとする解法"""
    N = int(input())
    event = []
    for _ in range(N):
        a, b = map(int, input().split())
        event.append([a, 1])
        event.append([a + b, -1])
    event.sort()

    cnt = [0] * (N + 1)
    date, people = 0, 0
    for day, diff in event:
        cnt[people] += day - date
        people += diff
        date = day

    print(*cnt[1:])


# solve_compress_and_imos()
solve_event_sort()
