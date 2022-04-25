"""
C - Cheese
https://atcoder.jp/contests/abc229/tasks/abc229_c
"""

N, W = map(int, input().split())
cheese = [list(map(int, input().split())) for _ in range(N)]
cheese.sort(reverse=True)

weight, s = 0, 0
for a, b in cheese:
    if weight + b <= W:
        weight += b
        s += a * b
    else:
        res = W - weight
        weight = W
        s += res * a
        break

print(s)
