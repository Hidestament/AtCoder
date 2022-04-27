"""
B - Star or Not
https://atcoder.jp/contests/abc225/tasks/abc225_b
"""

N = int(input())
degree = [0] * N
for _ in range(N - 1):
    a, b = map(int, input().split())
    degree[a - 1] += 1
    degree[b - 1] += 1

num_leaf = degree.count(1)
num_par = degree.count(N - 1)

print("Yes" if (num_par == 1) and (num_leaf == N - 1) else "No")
