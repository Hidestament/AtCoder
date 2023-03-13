"""
B - Call the ID Number
https://atcoder.jp/contests/abc293/tasks/abc293_b
"""

N = int(input())
A = list(map(int, input().split()))

not_called = set([i for i in range(1, N + 1)])
for i, a in enumerate(A, start=1):
    if i in not_called:
        not_called.discard(a)

print(len(not_called))
print(*sorted(not_called))
