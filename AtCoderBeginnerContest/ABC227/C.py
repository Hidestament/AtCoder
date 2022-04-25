"""
C - ABC conjecture
https://atcoder.jp/contests/abc227/tasks/abc227_c
"""

N = int(input())

cnt = 0
for a in range(1, int(pow(N, 1/3)) + 10):
    max_b = int(pow(N / a, 1/2)) + 10
    for b in range(a, max_b):
        if a > b:
            continue
        if a * b > N:
            break

        max_c = int(N / (a * b))
        cnt += max(0, max_c - b + 1)

print(cnt)
