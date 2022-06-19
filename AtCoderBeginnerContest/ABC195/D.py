"""
D - Shipping Center
https://atcoder.jp/contests/abc195/tasks/abc195_d
"""
from collections import deque

N, M, Q = map(int, input().split())
items = [list(map(int, input().split())) for _ in range(N)]
X = list(map(int, input().split()))
items.sort(key=lambda x: (-x[1], x[0]))

for _ in range(Q):
    left, right = map(int, input().split())
    left -= 1
    right -= 1

    using_box = [X[i] for i in range(M) if not (left <= i <= right)]
    using_box = deque(sorted(using_box))
    ans = 0
    for w, v in items:
        for _ in range(len(using_box)):
            now = using_box.popleft()
            if w <= now:
                ans += v
                break
            using_box.append(now)
        using_box = deque(sorted(using_box))
    print(ans)
