"""
B - Many Oranges
https://atcoder.jp/contests/abc195/tasks/abc195_b
"""

A, B, W = map(int, input().split())
W *= 10**3

ans = []
for x in range(10000000):
    min_weight = A * x
    max_weight = B * x
    if min_weight <= W <= max_weight:
        ans.append(x)

if ans:
    print(min(ans), max(ans))
else:
    print("UNSATISFIABLE")
