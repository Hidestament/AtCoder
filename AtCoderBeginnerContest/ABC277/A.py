"""
A - ^{-1}
https://atcoder.jp/contests/abc277/tasks/abc277_a
"""

N, X = map(int, input().split())
P = list(map(int, input().split()))

for i, p in enumerate(P, start=1):
    if X == p:
        print(i)
        exit()
