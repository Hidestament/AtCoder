"""
E - Just one
https://atcoder.jp/contests/abc226/tasks/abc226_e
出次数が1
    1. 連結成分ごとにかんがえれば良い
    2. 木だと, 向きつけできない
    3. 連結成分に2つ以上閉路があると, 向きつけできない
    4. 連結成分が1つあると, 2通りの向きつけができる
"""

import sys
sys.setrecursionlimit(10**7)


MOD = 998244353
N, M = map(int, input().split())
graph = [[] for _ in range(N)]
for _ in range(M):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    graph[u].append(v)
    graph[v].append(u)


def dfs(now, bef=-1):
    global num_cycle
    seen[now] = True
    for to in graph[now]:
        if to == bef:
            continue
        if seen[to]:
            num_cycle += 1
            continue
        dfs(to, now)


seen = [False] * N
ans = 1
for v in range(N):
    if seen[v]:
        continue

    num_cycle = 0
    dfs(v)
    ans *= 2 * (num_cycle == 2)
    ans %= MOD

print(ans)
