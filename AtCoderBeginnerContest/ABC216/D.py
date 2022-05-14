"""
D - Pair of Balls
https://atcoder.jp/contests/abc216/tasks/abc216_d
"""
from collections import defaultdict, deque

N, M = map(int, input().split())
balls = []
top_cnt = defaultdict(int)
ind = defaultdict(list)
dq = deque()  # 一番上を取り除ける筒
for i in range(M):
    k = int(input())
    a = list(map(int, input().split()))
    top_cnt[a[0]] += 1
    for num in a:
        ind[num].append(i)
    if top_cnt[a[0]] == 2:
        dq.append((ind[a[0]][0], ind[a[0]][1]))
    balls.append(deque(a))

while dq:
    i, j = dq.popleft()
    balls[i].popleft()
    if balls[i]:
        num = balls[i][0]
        top_cnt[num] += 1
        if top_cnt[num] == 2:
            dq.append((ind[num][0], ind[num][1]))

    balls[j].popleft()
    if balls[j]:
        num = balls[j][0]
        top_cnt[num] += 1
        if top_cnt[num] == 2:
            dq.append((ind[num][0], ind[num][1]))

print("Yes" if all(len(j) == 0 for j in balls) else "No")
