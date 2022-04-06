"""
B - Hit and Blow
問題リンク: https://atcoder.jp/contests/abc243/tasks/abc243_b
"""

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

one, two = 0, 0
for i in range(N):
    if A[i] == B[i]:
        one += 1
    for j in range(N):
        if (A[i] == B[j]) and (i != j):
            two += 1

print(one, two)
