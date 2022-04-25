"""
F - Ignore Operations
https://atcoder.jp/contests/abc249/tasks/abc249_f
参考: https://qiita.com/u2dayo/items/5565bf5e526ab3c6f7dc#f%E5%95%8F%E9%A1%8Cignore-operations
"""

from heapq import heappush, heappop


N, K = map(int, input().split())
operations = [[1, 0]] + [list(map(int, input().split())) for _ in range(N)]

hq = []  # 無視する操作
s = 0  # 無視しない操作の総和
ans = -float("INF")
for i in range(N + 1)[::-1]:
    t, x = operations[i]
    if t == 1:
        ans = max(ans, x + s)
        K -= 1
        if K < 0:  # K < 0 だと t = 1の操作をこれ以上無視できない
            break
    else:
        if x >= 0:
            s += x
        else:
            heappush(hq, -x)

    while len(hq) > K:  # 無視する操作の調整
        rm = -1 * heappop(hq)
        s += rm

print(ans)
