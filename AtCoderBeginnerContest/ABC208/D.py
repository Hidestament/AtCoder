"""
D - Shortest Path Queries 2
https://atcoder.jp/contests/abc208/tasks/abc208_d
"""

INF = 10**10
N, M = map(int, input().split())
graph = [[] for _ in range(N)]
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a - 1].append([b - 1, c])


def warshall_floyd(graph):
    n = len(graph)
    dist = [[INF] * n for _ in range(n)]

    # 初期状態: i -> i は距離0
    for i in range(n):
        dist[i][i] = 0

    # 初期状態: 隣接頂点のコストをdistに記録する
    for now in range(n):
        for to, cost in graph[now]:
            dist[now][to] = cost

    # DP
    ans = 0
    for k in range(n):  # 中継点
        for i in range(n):  # 始点
            for j in range(n):  # 終点
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
                if dist[i][j] < INF:
                    ans += dist[i][j]
    return ans


print(warshall_floyd(graph))
