"""
C - Doukasen
https://atcoder.jp/contests/abc223/tasks/abc223_c
"""

N = int(input())

total_time = 0
doukasen = []
for _ in range(N):
    a, b = map(int, input().split())
    total_time += a / b
    doukasen.append([a, b])

half_time = total_time / 2
now_time = 0
now_dist = 0
for a, b in doukasen:
    if now_time + a / b < half_time:
        now_time += a / b
        now_dist += a
    else:
        res_time = half_time - now_time
        print(now_dist + b * res_time)
        break
