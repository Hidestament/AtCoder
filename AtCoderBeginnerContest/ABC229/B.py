"""
B - Hard Calculation
https://atcoder.jp/contests/abc229/tasks/abc229_b
"""

A, B = map(str, input().split())
A = A[::-1]
B = B[::-1]

for a, b in zip(A, B):
    if int(a) + int(b) >= 10:
        print("Hard")
        exit()
print("Easy")
