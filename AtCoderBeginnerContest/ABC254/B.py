"""
B - Practical Computing
https://atcoder.jp/contests/abc254/tasks/abc254_b
"""

N = int(input())
A = []
for i in range(N):
    a = [1]
    for j in range(1, i + 1):
        if j == i:
            a.append(1)
        else:
            a.append(A[-1][j - 1] + A[-1][j])

    A.append(a)


for a in A:
    print(*a)
