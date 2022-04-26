"""
B - Counting Arrays
https://atcoder.jp/contests/abc226/tasks/abc226_b
"""

N = int(input())

ans = set()
for _ in range(N):
    l, *a = map(int, input().split())
    ans.add(tuple(a))

print(len(ans))
