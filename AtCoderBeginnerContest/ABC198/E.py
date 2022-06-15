"""
E - Unique Color
https://atcoder.jp/contests/abc198/tasks/abc198_e
"""
from collections import defaultdict
import sys

sys.setrecursionlimit(10**7)

N = int(input())
C = list(map(int, input().split()))
graph = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)


def dfs(now, bef=-1):
    counter[C[now]] += 1
    if counter[C[now]] == 1:
        ans.append(now + 1)

    for to in graph[now]:
        if to == bef:
            continue
        dfs(to, now)

    counter[C[now]] -= 1


ans = []
counter = defaultdict(int)
dfs(0)

ans.sort()
print(*ans, sep="\n")
