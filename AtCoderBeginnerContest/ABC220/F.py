"""
F - Distance Sums 2
https://atcoder.jp/contests/abc220/tasks/abc220_f
参考: https://atcoder.jp/contests/abc220/editorial/2693
"""
import sys

sys.setrecursionlimit(10**7)


N = int(input())
graph = [[] for _ in range(N)]
for _ in range(N - 1):
    u, v = map(int, input().split())
    graph[u - 1].append(v - 1)
    graph[v - 1].append(u - 1)


def dfs(now, bef=-1):
    for to in graph[now]:
        if to == bef:
            continue
        dist[to] = dist[now] + 1
        dfs(to, now)
        subtree[now] += subtree[to]


def ans_dfs(now, bef=-1):
    if now != 0:
        ans[now] = ans[bef] - subtree[now] + (N - subtree[now])
    for to in graph[now]:
        if to == bef:
            continue
        ans_dfs(to, now)


dist, ans = [0] * N, [0] * N
subtree = [1] * N
dfs(0)

ans[0] = sum(dist)
ans_dfs(0)

print(*ans)
