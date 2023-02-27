"""
F - Teleporter and Closed off
https://atcoder.jp/contests/abc291/tasks/abc291_f
"""

INF = float("inf")


N, M = map(int, input().split())
S = [input() for _ in range(N)]

dist = [INF] * N
dist[0] = 0
for i in range(N - 1):
    for to, s in enumerate(S[i], start=1):
        if s == "1":
            dist[i + to] = min(dist[i + to], dist[i] + 1)

rS = [["0"] * M for _ in range(N)]
for i in range(N):
    for to, s in enumerate(S[i], start=1):
        if s == "1":
            rS[i + to][to - 1] = "1"

rdist = [INF] * N
rdist[-1] = 0
for i in range(1, N)[::-1]:
    for to, s in enumerate(rS[i], start=1):
        if s == "1":
            rdist[i - to] = min(rdist[i - to], rdist[i] + 1)


for k in range(1, N - 1):
    ans = INF

    for m in range(1, M):
        bridge_prev = k - m

        # 0 -> bridge_prevのパスがない場合は駄目
        if dist[bridge_prev] == INF:
            continue

        for to, s in enumerate(S[bridge_prev], start=1):
            if s == "0":
                continue

            bridge_to = bridge_prev + to

            if bridge_to <= k:
                continue
            if rdist[bridge_to] == INF:
                continue

            ans = min(ans, dist[bridge_prev] + 1 + rdist[bridge_to])

    print(-1 if ans == INF else ans)
