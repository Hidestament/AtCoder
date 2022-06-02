"""
E - Ring MST
https://atcoder.jp/contests/abc210/tasks/abc210_e
参考: https://note.com/momomo0214/n/nf95deeaddd75
"""
from math import gcd


N, M = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(M)]
edges.sort(key=lambda x: x[1])

ans = 0
for a, c in edges:
    g = gcd(N, a)
    ans += c * (N - g)
    N = g
    if N == 1:
        break

print(ans if N == 1 else -1)
