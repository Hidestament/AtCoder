"""
C - Graph Isomorphism
https://atcoder.jp/contests/abc232/tasks/abc232_c
"""

from itertools import permutations


N, M = map(int, input().split())
edges1 = set()
for _ in range(M):
    a, b = map(int, input().split())
    a, b = min(a-1, b-1), max(a-1, b-1)
    edges1.add((a, b))

edges2 = []
for _ in range(M):
    a, b = map(int, input().split())
    edges2.append([a-1, b-1])


def convert_edges(P):
    edges = set()
    for i, j in edges2:
        i, j = P[i], P[j]
        edges.add((min(i, j), max(i, j)))
    return edges


for per in permutations(range(N)):
    isomorphism_edges = convert_edges(per)
    if isomorphism_edges == edges1:
        print("Yes")
        break
else:
    print("No")
