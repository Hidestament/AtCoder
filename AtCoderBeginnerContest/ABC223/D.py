"""
D - Restricted Permutation
https://atcoder.jp/contests/abc223/tasks/abc223_d
辞書順最小のトポロジカルソート
"""

from heapq import heapify, heappop, heappush


N, M = map(int, input().split())
graph = [[] for _ in range(N)]
indeg = [0] * N
for _ in range(M):
    a, b = map(int, input().split())
    graph[a - 1].append(b - 1)
    indeg[b - 1] += 1

for i in range(N):
    graph[i] = sorted(graph[i])


def topological_sort(graph, indeg):
    ans = []
    hq = [v for v in range(len(graph)) if indeg[v] == 0]
    heapify(hq)
    while hq:
        now = heappop(hq)
        ans.append(now + 1)
        for to in graph[now]:
            indeg[to] -= 1
            if indeg[to] == 0:
                heappush(hq, to)
    return ans


topological = topological_sort(graph, indeg)
if len(topological) == N:
    print(*topological)
else:
    print(-1)
