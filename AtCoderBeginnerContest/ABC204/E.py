"""
E - Rush Hour 2
https://atcoder.jp/contests/abc204/tasks/abc204_e
"""
from heapq import heappush, heappop


N, M = map(int, input().split())
graph = [[] for _ in range(N)]
for _ in range(M):
    a, b, c, d = map(int, input().split())
    graph[a - 1].append([b - 1, c, d])
    graph[b - 1].append([a - 1, c, d])


def calc_opt_time(min_t, c, d):
    sqrt_d = int(d**0.5)
    opt_t = min_t + c + (d // (min_t + 1))
    for t in range(sqrt_d - 10, sqrt_d + 10):
        if min_t <= t:
            opt_t = min(opt_t, t + c + (d // (t + 1)))
    return opt_t


INF = float("inf")
dist = [INF] * N
dist[0] = 0
flag = [False] * N
hq = [[0, 0]]
while hq:
    _, now = heappop(hq)
    if flag[now]:
        continue
    flag[now] = True
    for to, c, d in graph[now]:
        if flag[to]:
            continue
        opt_time = calc_opt_time(dist[now], c, d)
        if opt_time < dist[to]:
            dist[to] = opt_time
            heappush(hq, (dist[to], to))

print(dist[N - 1] if dist[N - 1] < INF else -1)
