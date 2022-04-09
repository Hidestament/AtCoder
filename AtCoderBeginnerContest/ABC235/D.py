"""
D - Multiply and Rotate
https://atcoder.jp/contests/abc235/tasks/abc235_d
"""

from collections import deque


a, N = map(int, input().split())

used = set([1])
dq = deque([[1, 0]])
while dq:
    x, cnt = dq.popleft()
    if len(str(x)) > len(str(N)):
        continue

    if x == N:
        print(cnt)
        exit()

    # 操作1: multiple
    if a*x not in used:
        used.add(a*x)
        dq.append([a*x, cnt+1])

    # 操作2: rotate
    if (x > 10) and (x % 10 != 0):
        x = str(x)
        x = int(x[-1] + x[:-1])
        if x not in used:
            used.add(x)
            dq.append([x, cnt+1])

print(-1)
