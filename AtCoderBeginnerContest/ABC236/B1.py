"""
B - Who is missing?
https://atcoder.jp/contests/abc236/tasks/abc236_b
"""

from collections import Counter


N = int(input())
A = list(map(int, input().split()))
cnt = Counter(A)

for key, value in cnt.items():
    if value == 3:
        print(key)
        break
