"""Python AC, Pypy TLE
E - Ranges on Tree
https://atcoder.jp/contests/abc240/tasks/abc240_e
DFSで葉から[L, R]の値を決めていく
"""

import sys
sys.setrecursionlimit(10**7)


N = int(input())
graph = [[] for _ in range(N)]
for _ in range(N - 1):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    graph[u].append(v)
    graph[v].append(u)

left, right = [10**10] * N, [-10**10] * N
num_leaves = 0


def dfs(now, bef=-1):
    global num_leaves
    flag = True
    for to in graph[now]:
        if to == bef:
            continue
        dfs(to, now)

        # nowの子供toの部分木全て計算したら, 頂点nowの値の更新
        left[now] = min(left[now], left[to])
        right[now] = max(right[now], right[to])
        flag = False

    # 現在のnodeが葉だったら
    if flag:
        num_leaves += 1
        left[now] = right[now] = num_leaves


dfs(0)
for L, R in zip(left, right):
    print(L, R)
