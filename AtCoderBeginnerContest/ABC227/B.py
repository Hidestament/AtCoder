"""
B - KEYENCE building
https://atcoder.jp/contests/abc227/tasks/abc227_b
"""

N = int(input())
S = list(map(int, input().split()))

possible = set()
for a in range(1, 1001):
    for b in range(1, 1001):
        s = 4*a*b + 3*a + 3*b
        possible.add(s)

cnt = sum(s not in possible for s in S)
print(cnt)
