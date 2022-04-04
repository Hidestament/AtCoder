"""
E - King Bombee
問題リンク: https://atcoder.jp/contests/abc244/tasks/abc244_e
"""

N, M, K, S, T, X = map(int, input().split())
mod = 998244353
S, T, X = S-1, T-1, X-1

graph = [[] for _ in range(N)]
for _ in range(M):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    graph[u].append(v)
    graph[v].append(u)

# DP[k][v][parity]: 長さkのパスの中で頂点vで終わるモノの個数.
# ここで, parity=0なら偶数回, parity=1なら奇数回, 頂点Xを通っている
DP = [[[0, 0] for _ in range(N)] for _ in range(K+1)]
DP[0][S][0] = 1

for k in range(1, K+1):
    for now in range(N):
        for to in graph[now]:
            if to == X:
                DP[k][to][0] += DP[k-1][now][1]
                DP[k][to][0] %= mod

                DP[k][to][1] += DP[k-1][now][0]
                DP[k][to][1] %= mod
            else:
                DP[k][to][0] += DP[k-1][now][0]
                DP[k][to][0] %= mod

                DP[k][to][1] += DP[k-1][now][1]
                DP[k][to][1] %= mod

print(DP[K][T][0])
