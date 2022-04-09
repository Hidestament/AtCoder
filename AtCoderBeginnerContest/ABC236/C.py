"""
C - Route Map
https://atcoder.jp/contests/abc236/tasks/abc236_c
"""

N, M = map(int, input().split())
S = list(map(str, input().split()))
T = set(list(map(str, input().split())))

for s in S:
    print("Yes" if s in T else "No")
