"""
D - Snuke Prime
https://atcoder.jp/contests/abc188/tasks/abc188_d
"""

from collections import defaultdict


N, C = map(int, input().split())
event = defaultdict(list)
for _ in range(N):
    a, b, c = map(int, input().split())
    event[a].append(c)
    event[b + 1].append(-c)


event_keys = [0] + sorted(event.keys()) + [10**10]

all_sum = 0
ans = 0
for i, day in enumerate(event_keys[1:], start=1):
    # その日までの合計料金の計算
    ans += min(C, all_sum) * (day - event_keys[i - 1])

    # サービス料金の更新
    all_sum += sum(event[day])

print(ans)
