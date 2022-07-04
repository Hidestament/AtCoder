"""
C - Mandarin Orange
https://atcoder.jp/contests/abc189/tasks/abc189_c
"""

N = int(input())
A = list(map(int, input().split()))

ans = 0
for left in range(N):
    min_element = A[left]
    for right in range(left, N):
        min_element = min(min_element, A[right])
        ans = max(ans, (right - left + 1) * min_element)
print(ans)
