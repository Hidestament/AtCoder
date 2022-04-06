"""
E - Edge Deletion
問題リンク: https://atcoder.jp/contests/abc243/tasks/abc243_e
"""

N, M = map(int, input().split())
graph = [[] for _ in range(N)]
edges = []
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a-1].append((b-1, c))
    graph[b-1].append((a-1, c))
    edges.append([a-1, b-1, c])


INF = 10**10


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
    for k in range(n):  # 中継点
        for i in range(n):  # 始点
            for j in range(n):  # 終点
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    return dist


dist = warshall_floyd(graph)

# (辺の本数 - 残さないといけない辺) が 削除できる辺の個数
# 辺(i, j, w) に対して, i -> j の最短路が, 辺(i, j, w)のみなら残さないといけない
ans = M
for now, to, cost in edges:
    # 辺(now, to, cost)を使用しない最短路を全探索する
    # costより小さい経路が存在しなかったら, その辺は残す必要がある
    flag = True
    for k in range(N):
        if (k == now) or (k == to):
            continue
        d = dist[now][k] + dist[k][to]
        if d <= cost:
            flag = False

    if flag:
        ans -= 1

print(ans)
