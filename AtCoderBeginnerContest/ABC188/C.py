"""
C - ABC Tournament
https://atcoder.jp/contests/abc188/tasks/abc188_c
"""

N = int(input())
A = list(map(int, input().split()))

left_A = A[:pow(2, N - 1)]
right_A = A[pow(2, N - 1):]

left_A_max = max(left_A)
right_A_max = max(right_A)

if left_A_max < right_A_max:
    print(A.index(left_A_max) + 1)
else:
    print(A.index(right_A_max) + 1)
