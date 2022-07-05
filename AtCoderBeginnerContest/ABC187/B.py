"""
B - Gentle Pairs
https://atcoder.jp/contests/abc187/tasks/abc187_b
"""

N = int(input())
points = [list(map(int, input().split())) for _ in range(N)]

cnt = 0
for i in range(N - 1):
    xi, yi = points[i]
    for j in range(i + 1, N):
        xj, yj = points[j]
        if abs((yi - yj) / (xi - xj)) <= 1:
            cnt += 1

print(cnt)
