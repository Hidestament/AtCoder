"""Python -> AC
F - Endless Walk
問題リンク: https://atcoder.jp/contests/abc245/tasks/abc245_f

強成分連結分解して, その成分にたどり着ける頂点を列挙する
SCCの部分をScipy実装
"""

from collections import Counter
from scipy.sparse.csgraph import connected_components
from scipy.sparse import csr_matrix
import sys
sys.setrecursionlimit(10**6)


N, M = map(int, input().split())
i, j = [], []
edges = []
for _ in range(M):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    i.append(u)
    j.append(v)
    edges.append([u, v])

d = [1] * M

# scipyで強連結成分分解する
csr = csr_matrix((d, (i, j)), (N, N))
n, label = connected_components(csr, connection="strong")

# 強連結成分分解した新しいグラフを作成する
cnt = Counter(label)

scc_graph = [set() for _ in range(n)]
for u, v in edges:
    scc_u = label[u]
    scc_v = label[v]
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


seen = [False] * n
reach_size = [cnt[v] for v in range(n)]
for v in range(n):
    if seen[v]:
        continue
    dfs(v)


print(N - reach_size.count(1))
