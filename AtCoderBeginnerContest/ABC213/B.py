"""
B - Booby Prize
https://atcoder.jp/contests/abc213/tasks/abc213_b
"""
N = int(input())
A = list(map(int, input().split()))
A = [(a, i) for i, a in enumerate(A)]
A.sort(reverse=True)
print(A[1][1] + 1)
