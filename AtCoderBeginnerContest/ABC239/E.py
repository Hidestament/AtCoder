"""
E - Subtree K-th Max
https://atcoder.jp/contests/abc239/tasks/abc239_e
K <= 20なので, 木DPで大きい方から20個の頂点を常に持っておく
"""

import sys
sys.setrecursionlimit(10**7)


N, Q = map(int, input().split())
X = list(map(int, input().split()))
graph = [[] for _ in range(N)]
for _ in range(N-1):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    graph[u].append(v)
    graph[v].append(u)


subtree = [[X[i]] for i in range(N)]


def dfs(now, bef=-1):
    for to in graph[now]:
        if to == bef:
            continue
        dfs(to, now)

        # 子toの部分木の計算が終わったら, merge
        subtree[now] = sorted(subtree[now] + subtree[to], reverse=True)[:20]


dfs(0)
for _ in range(Q):
    v, k = map(int, input().split())
    print(subtree[v-1][k-1])
