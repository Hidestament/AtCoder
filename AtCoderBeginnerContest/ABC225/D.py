"""
D - Play Train
https://atcoder.jp/contests/abc225/tasks/abc225_d
"""

N, Q = map(int, input().split())

prev = [-1] * N  # 前の電車
to = [-1] * N  # 後ろの電車


def prev_dfs(now):
    linked = []
    while prev[now] != -1:
        now = prev[now]
        linked.append(now + 1)
    return linked[::-1]


def to_dfs(now):
    linked = []
    while to[now] != -1:
        now = to[now]
        linked.append(now + 1)
    return linked


for _ in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 1:
        x, y = q[1] - 1, q[2] - 1
        prev[y], to[x] = x, y
    elif q[0] == 2:
        x, y = q[1] - 1, q[2] - 1
        to[x], prev[y] = -1, -1
    else:
        x = q[1]
        ans = prev_dfs(x - 1) + [x] + to_dfs(x - 1)
        print(len(ans), *ans)
