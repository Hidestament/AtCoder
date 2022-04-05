"""Python, Pypy -> TLE
F - Endless Walk
問題リンク: https://atcoder.jp/contests/abc245/tasks/abc245_f

強連結成分分解して, その成分にたどり着ける頂点を列挙する
SCCを自前実装 -> TLE
"""

from collections import Counter
import sys
sys.setrecursionlimit(10**6)


N, M = map(int, input().split())
graph = [[] for _ in range(N)]
rgraph = [[] for _ in range(N)]
edges = []
for _ in range(M):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    graph[u].append(v)
    rgraph[v].append(u)
    edges.append([u, v])


def scc(N, G, RG):
    """Strongly-Connected Components

    Args:
        N (int): number of vertex_
        G (List[list(int)]): adjacent list
        RG (List[list(int)]): reverse adjacent list

    """

    def dfs(now):
        seen[now] = 1
        for to in G[now]:
            if not seen[to]:
                dfs(to)
        order.append(now)

    def rdfs(now, col):
        seen[now] = 1
        group[now] = col
        for to in RG[now]:
            if not seen[to]:
                rdfs(to, col)

    order, seen = [], [0] * N

    for v in range(N):
        if not seen[v]:
            dfs(v)

    group, seen = [None] * N, [0] * N
    label = 0
    for v in order[::-1]:
        if not seen[v]:
            rdfs(v, label)
            label += 1

    return label, group


# 強連結成分分解した新しいグラフを作成する
label, group = scc(N, graph, rgraph)
cnt = Counter(group)

scc_graph = [set() for _ in range(label)]
for u, v in edges:
    scc_u = group[u]
    scc_v = group[v]
    if scc_u == scc_v:
        continue
    scc_graph[scc_u].add(scc_v)


# DFSでトポロジカルソートしながら, 答えを計算
def dfs(now):
    seen[now] = True
    for to in scc_graph[now]:
        if seen[to]:
            continue
        dfs(to)

    for to in scc_graph[now]:
        reach_size[now] = max(reach_size[to], reach_size[now])


seen = [False] * label
reach_size = [cnt[v] for v in range(label)]
for v in range(label):
    if seen[v]:
        continue
    dfs(v)


print(N - reach_size.count(1))
