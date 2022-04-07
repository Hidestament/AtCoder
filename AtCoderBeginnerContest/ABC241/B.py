"""
B - Pasta
https://atcoder.jp/contests/abc241/tasks/abc241_b
"""

from collections import Counter


N, M = map(int, input().split())
A = Counter(list(map(int, input().split())))
B = list(map(int, input().split()))

flag = True
for b in B:
    if A[b] != 0:
        A[b] -= 1
    else:
        flag = False

print("Yes" if flag else "No")
