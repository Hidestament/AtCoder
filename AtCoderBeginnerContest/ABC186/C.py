"""
C - Unlucky 7
https://atcoder.jp/contests/abc186/tasks/abc186_c
"""

N = int(input())

cnt = 0
for i in range(1, N + 1):
    if "7" in str(i):
        continue

    if "7" in oct(i):
        continue

    cnt += 1

print(cnt)
