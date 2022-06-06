"""
E - Xor Distances
https://atcoder.jp/contests/abc201/tasks/abc201_e
"""
from collections import deque


MOD = 10**9 + 7
N = int(input())
graph = [[] for _ in range(N)]
for _ in range(N - 1):
    u, v, w = map(int, input().split())
    graph[u - 1].append([v - 1, w])
    graph[v - 1].append([u - 1, w])


dist = [-1] * N
dist[0] = 0
dq = deque([0])
while dq:
    now = dq.popleft()
    for to, w in graph[now]:
        if dist[to] != -1:
            continue
        dist[to] = dist[now] ^ w
        dq.append(to)

one_bit_cnt = [0] * 70
for d in dist:
    for k in range(70):
        if d & (1 << k):
            one_bit_cnt[k] += 1

ans = 0
for k in range(70):
    ans += pow(2, k) * one_bit_cnt[k] * (N - one_bit_cnt[k])
    ans %= MOD
print(ans)
