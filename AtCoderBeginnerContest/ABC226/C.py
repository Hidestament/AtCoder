"""
C - Martial artist
https://atcoder.jp/contests/abc226/tasks/abc226_c
"""
import sys
sys.setrecursionlimit(10**7)


N = int(input())
time, A = [], []
for _ in range(N):
    t, k, *a = map(int, input().split())
    time.append(t)
    A.append(sorted(a))


def dfs(now):
    global ans
    for a in A[now]:
        if (a - 1) not in get:
            dfs(a - 1)
    get.add(now)
    ans += time[now]


ans = 0
get = set()
dfs(N - 1)

print(ans)
