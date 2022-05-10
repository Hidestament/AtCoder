"""
E - Red and Blue Tree
https://atcoder.jp/contests/abc222/tasks/abc222_e
参考: https://atcoder.jp/contests/abc222/editorial/2751
"""
N, M, K = map(int, input().split())
A = list(map(lambda x: int(x) - 1, input().split()))
MOD = 998244353
graph = [[] for _ in range(N)]
for i in range(N - 1):
    x, y = map(lambda x: int(x) - 1, input().split())
    graph[x].append((y, i))
    graph[y].append((x, i))


def dfs(now, bef, end):
    if now == end:
        return
    for to, i in graph[now]:
        if to == bef:
            continue
        pi[to] = [now, i]
        dfs(to, now, end)


# 使用する辺の本数を計算
cnt = [0] * (N - 1)
pi = [-1] * N
for i in range(1, M):
    start, end = A[i - 1], A[i]
    dfs(start, -1, end)
    # 経路復元を行い, 使用した辺の回数を計算する
    now = end
    while now != start:
        now, i = pi[now]
        cnt[i] += 1

S = sum(cnt)
if ((S + K) % 2 != 0) or (S + K < 0):
    print(0)
    exit()

S = (S + K) // 2
# DP[i][s]: i番目までを選んで, 和をsにする方法の数
DP = [[0] * (S + 1) for _ in range(N)]
DP[0][0] = 1

for i in range(1, N):
    c = cnt[i - 1]
    for s in range(S + 1):
        # i番目の辺を選ぶとき
        if s - c >= 0:
            DP[i][s] += DP[i - 1][s - c]

        # 選ばないとき
        DP[i][s] += DP[i - 1][s]
        DP[i][s] %= MOD

print(DP[-1][-1])
