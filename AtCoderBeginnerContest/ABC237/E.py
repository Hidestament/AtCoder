"""
E - Skiing
https://atcoder.jp/contests/abc237/tasks/abc237_e
1. 辺のコストを-1倍して最短経路に帰着
2. H=ポテンシャルなので, ポテンシャル変換して辺の重みを全て非負にする
"""

from heapq import heappop, heappush


N, M = map(int, input().split())
H = list(map(int, input().split()))
graph = [[] for _ in range(N)]
for _ in range(M):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    graph[u].append(v)
    graph[v].append(u)

hq = [[0, 0]]
dist = [-1] * N
while hq:
    cost, now = heappop(hq)
    if dist[now] != -1:
        continue
    # ここで値を確定させる
    dist[now] = cost

    for to in graph[now]:
        if dist[to] != -1:
            continue
        if H[now] >= H[to]:
            heappush(hq, [cost, to])
        else:
            heappush(hq, [cost + H[to] - H[now], to])

ans = 0
for to in range(N):
    d = dist[to] - H[0] + H[to]
    ans = max(ans, -d)
print(ans)
