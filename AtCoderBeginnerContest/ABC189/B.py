"""
B - Alcoholic
https://atcoder.jp/contests/abc189/tasks/abc189_b
"""

N, X = map(int, input().split())

X *= 100
vol = 0
for i in range(1, N + 1):
    v, p = map(int, input().split())
    vol += v * p
    if vol > X:
        print(i)
        exit()

print(-1)
