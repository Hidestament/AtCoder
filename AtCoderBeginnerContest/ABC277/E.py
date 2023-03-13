"""
E - Crystal Switches
https://atcoder.jp/contests/abc277/tasks/abc277_e
"""
from collections import deque


N, M, K = map(int, input().split())
no_switch_graph = [[] for _ in range(N)]
on_switch_graph = [[] for _ in range(N)]
for _ in range(M):
    u, v, a = map(int, input().split())
    if a == 1:
        no_switch_graph[u - 1].append(v - 1)
        no_switch_graph[v - 1].append(u - 1)
    else:
        on_switch_graph[u - 1].append(v - 1)
        on_switch_graph[v - 1].append(u - 1)

s = set(list(map(lambda x: int(x) - 1, input().split())))

# [v, dist, switch]: 現在の頂点vと, switchの状態
# 0-> switch押して無い, 1-> switch押した状態
dq = deque()
dq.append([0, 0, 0])

# dist[v][switch]: スイッチの状態switchにおける頂点vの距離
dist = [[-1] * 2 for _ in range(N)]
while dq:
    now, d, switch = dq.popleft()
    if dist[now][switch] != -1:
        continue
    dist[now][switch] = d

    if now in s:
        # switchを押したケース
        for to in on_switch_graph[now]:
            if dist[to][1] != -1:
                continue
            dq.append([to, d + 1, 1])
        # switchを押さないケース
        for to in no_switch_graph[now]:
            if dist[to][0] != -1:
                continue
            dq.append([to, d + 1, 0])
    else:
        if switch == 0:
            for to in no_switch_graph[now]:
                if dist[to][0] != -1:
                    continue
                dq.append([to, d + 1, 0])
        else:
            for to in on_switch_graph[now]:
                if dist[to][1] != -1:
                    continue
                dq.append([to, d + 1, 1])


if dist[-1] == [-1, -1]:
    print(-1)
else:
    if dist[-1][0] == -1:
        print(dist[-1][1])
    elif dist[-1][1] == -1:
        print(dist[-1][0])
    else:
        print(min(dist[-1]))
