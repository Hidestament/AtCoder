"""
D - RGB Coloring 2
https://atcoder.jp/contests/abc199/tasks/abc199_d
参考: https://note.com/momomo0214/n/nb84b95fdd29e
"""
import sys

sys.setrecursionlimit(10**7)

N, M = map(int, input().split())
graph = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)


# 連結成分ごとに考える
def dfs(now, bef=-1):
    flag[now] = 1
    c.append(now)
    for to in graph[now]:
        if flag[to]:
            continue
        dfs(to, now)


flag = [0] * N
cc = []  # connected_components: 連結成分
for v in range(N):
    if flag[v]:
        continue
    c = []
    dfs(v)
    cc.append(c)


def calc_coloring(i):
    global pattern
    if i == len(c):
        pattern += 1
        return

    v = c[i]
    for color in range(3):
        if all(colors[to] != color for to in graph[v]):
            colors[v] = color
            calc_coloring(i + 1)
            colors[v] = -1


# 連結成分ごとに実際に色塗っている
# このとき, DFSでの探索順で塗っていくことで正しく計算できる
ans = 1
for c in cc:
    colors = [-1] * N
    colors[c[0]] = 0  # 0番目の頂点は, 0色で固定する
    pattern = 0
    calc_coloring(1)
    ans *= 3 * pattern
print(ans)
