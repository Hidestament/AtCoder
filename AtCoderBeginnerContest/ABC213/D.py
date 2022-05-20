"""
D - Takahashi Tour
https://atcoder.jp/contests/abc213/tasks/abc213_d
"""
import sys

sys.setrecursionlimit(10**7)

N = int(input())
graph = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)

for v in range(N):
    graph[v] = sorted(graph[v])


def dfs(now):
    seen[now] = 1
    euler_tour.append(now + 1)
    for to in graph[now]:
        if seen[to]:
            continue
        dfs(to)
        euler_tour.append(now + 1)


seen = [0] * N
euler_tour = []
dfs(0)

print(*euler_tour)
