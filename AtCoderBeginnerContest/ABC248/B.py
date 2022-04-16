"""
B - Slimes
https://atcoder.jp/contests/abc248/tasks/abc248_b
"""

A, B, K = map(int, input().split())

if B <= A:
    print(0)
    exit()

cnt = 1
while True:
    A *= K
    if B <= A:
        print(cnt)
        break
    cnt += 1
