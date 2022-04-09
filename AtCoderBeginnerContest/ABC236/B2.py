"""
B - Who is missing?
https://atcoder.jp/contests/abc236/tasks/abc236_b
Xorで解く
"""

N = int(input())
A = list(map(int, input().split()))

ans = 0
for a in A:
    ans ^= a
print(ans)
