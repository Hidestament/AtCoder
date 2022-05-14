"""
F - Max Sum Counting
https://atcoder.jp/contests/abc216/tasks/abc216_f
"""

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
MOD = 998244353

AB = sorted(zip(A, B))

# DP[i][s]: i番目まで選んだときに, Bの総和がsとなるようなものの個数
DP = [[0] * 5005 for _ in range(N + 1)]
DP[0][0] = 1

ans = 0
for i in range(1, N + 1):
    a, b = AB[i - 1]
    for s in range(5005):
        # AB[i-1]を選ぶとき
        if s - b >= 0:
            DP[i][s] += DP[i - 1][s - b]
            DP[i][s] %= MOD
            if s <= a:
                ans += DP[i][s]
                ans %= MOD

        # AB[i-1]を選ばないとき
        DP[i][s] += DP[i - 1][s]
        DP[i][s] %= MOD

print(ans)
