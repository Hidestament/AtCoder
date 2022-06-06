"""
B - 200th ABC-200
https://atcoder.jp/contests/abc200/tasks/abc200_b
"""

N, K = map(int, input().split())
for _ in range(K):
    if N % 200 == 0:
        N //= 200
    else:
        N = int(str(N) + "200")

print(N)
