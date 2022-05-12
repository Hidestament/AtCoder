"""
B - Base K
https://atcoder.jp/contests/abc220/tasks/abc220_b
"""
K = int(input())
A, B = map(str, input().split())

print(int(A, K) * int(B, K))
