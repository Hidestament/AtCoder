"""
B - Everyone is Friends
https://atcoder.jp/contests/abc272/tasks/abc272_b
"""
import sys
from itertools import combinations

input = sys.stdin.readline

N, M = map(int, input().split())
X = []
for _ in range(M):
    x = list(map(int, input().split()))
    X.append(set(x[1:]))

flag = True
for a, b in combinations(range(N), r=2):
    a += 1
    b += 1

    if any((a in x) and (b in x) for x in X):
        continue
    else:
        flag = False
        break

print("Yes" if flag else "No")
