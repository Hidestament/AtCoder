"""
F - Select Edges
https://atcoder.jp/contests/abc259/tasks/abc259_f
"""

import sys

sys.setrecursionlimit(10**7)

N = int(input())
D = list(map(int, input().split()))
graph = [[] for _ in range(N)]
for _ in range(N - 1):
    u, v, w = map(int, input().split())
    graph[u - 1].append((v - 1, w))
    graph[v - 1].append((u - 1, w))


# DP[i][flag]: 部分木iの辺の選び方の最大値. where flag=1なら変をdi以下, flag=0ならdi未満
DP = [[0, 0] for _ in range(N)]


def dfs(now=0, bef=-1):
    for to, _ in graph[now]:
        if to == bef:
            continue
        dfs(to, bef=now)
        DP[now][0] += DP[to][1]
        DP[now][1] += DP[to][1]

    if D[now] == 0:
        return

    delta = [
        DP[to][0] + w - DP[to][1] for to, w in graph[now] if to != bef and D[to] != 0
    ]
    delta.sort(reverse=True)

    cnt = D[now]
    for d in delta:
        if (d < 0) or (cnt == 0):
            break

        if cnt == 1:
            DP[now][1] += d
            cnt -= 1
        else:
            DP[now][1] += d
            DP[now][0] += d
            cnt -= 1


dfs()
print(max(DP[0]))
