"""
D - Jumping Takahashi 2
https://atcoder.jp/contests/abc257/tasks/abc257_d
"""

from collections import deque


N = int(input())
points = [list(map(int, input().split())) for _ in range(N)]


def dist(i, j):
    xi, yi, _ = points[i]
    xj, yj, _ = points[j]
    return abs(xi - xj) + abs(yi - yj)


def bfs(start, s):
    dq = deque([start])
    res = deque([i for i in range(N) if i != start])
    while dq:
        now = dq.popleft()
        for _ in range(len(res)):
            to = res.popleft()
            if points[now][2] * s >= dist(now, to):
                dq.append(to)
            else:
                res.append(to)
    return len(res) == 0


def check(s):
    for start in range(N):
        if bfs(start, s):
            return True
    return False


left, right = 0, 10**10
while (right - left) > 1:
    mid = (left + right) // 2
    if check(mid):
        right = mid
    else:
        left = mid

print(right)
